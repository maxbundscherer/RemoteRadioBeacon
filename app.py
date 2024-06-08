from flask import Flask, render_template, url_for, jsonify, request

from backend.ConfigService import ConfigService
from backend.HamService import HamService
from backend.TestService import TestService

config_service: ConfigService = ConfigService()
test_service: TestService = TestService()
ham_service: HamService = HamService(config_service=config_service)

app = Flask(
    __name__
)


@app.route('/')
def route_index():
    page_html = "<p>Please make a selection:</p><ul>"
    for url_title, url_target in [
        ('Control', url_for('route_control')),
        ('Test-UI', url_for('route_test_ui')),
        ('About', url_for('route_about')),
    ]:
        page_html += f'<li><a href="{url_target}">{url_title}</a></li>'
    page_html += "</ul>"
    page_html += "<h3>Overview</h3>"
    page_html += '<table class="tab-content">'
    page_html += f'<tr><td>Startup Time</td><td>{config_service.get_startup_time()}</td></tr>'
    page_html += '<tr><td><br></td><td></td></tr>'
    page_html += f'<tr><td>TX Locator</td><td>{config_service.get_config().tx_locator}</td></tr>'
    page_html += '<tr><td><br></td><td></td></tr>'
    page_html += f'<tr><td>Ant Rotator</td><td>{config_service.get_config().ant_rotator_service}</td></tr>'
    page_html += f'<tr><td>Radio Control</td><td>{config_service.get_config().radio_control_service}</td></tr>'
    page_html += '<tr><td><br></td><td></td></tr>'
    page_html += f'<tr><td>TX-Wav Sampling-Rate (Hz)</td><td>{config_service.get_local_wav_tx_sr()}</td></tr>'
    page_html += f'<tr><td>TX-Wav Duration (sec)</td><td>{config_service.get_local_wav_tx_duration()}</td></tr>'
    page_html += '</table>'
    return render_template('simple_html.html',
                           site_app_title=config_service.get_app_title(),
                           site_app_version=config_service.get_app_version(),
                           site_title='Home',
                           page_html=page_html,
                           )


@app.route('/control', methods=['GET', 'POST'])
def route_control():
    if request.method == 'POST':
        data = request.get_data()
        print(data)
        print(request.form['description'])
        test_service.set_test_description(
            request.form['description']
        )
        test_service.set_test_int(
            int(request.form['test_int'])
        )

    return render_template('control.html',
                           site_app_title=config_service.get_app_title(),
                           site_app_version=config_service.get_app_version(),
                           site_title='Control',
                           page_test_int=test_service.get_test_int(),
                           page_test_description=test_service.get_test_description(),
                           )


@app.route('/test/ui', methods=['GET', 'POST'])
def route_test_ui():
    if request.method == 'POST':
        data = request.get_data()
        print(data)
        print(request.form['description'])
        test_service.set_test_description(
            request.form['description']
        )
        test_service.set_test_int(
            int(request.form['test_int'])
        )

    return render_template('test_ui.html',
                           site_app_title=config_service.get_app_title(),
                           site_app_version=config_service.get_app_version(),
                           site_title='Test-UI',
                           page_test_int=test_service.get_test_int(),
                           page_test_description=test_service.get_test_description(),
                           )


@app.route('/about')
def route_about():
    return render_template('simple_content.html',
                           site_app_title=config_service.get_app_title(),
                           site_app_version=config_service.get_app_version(),
                           site_title='About',
                           page_content='The quick brown fox jumps over the lazy dog - 73 de DD7MB',
                           )


@app.route('/api/test')
def route_api_test():
    return jsonify(
        test_service.get_test_item()
    )


@app.route('/api/ham/ant_rotator', methods=["GET", "POST"])
def route_api_ham_ant_rotator():
    if request.method == 'POST':
        content = request.get_json()

        if 'azimuth' in content:
            ham_service.set_ant_rotator_azimuth(content['azimuth'])

        if 'elevation' in content:
            ham_service.set_ant_rotator_elevation(content['elevation'])

        return "OK"

    return jsonify(
        ham_service.get_ant_rotator_state()
    )


@app.route('/api/ham/radio')
def route_api_ham_radio():
    return jsonify(
        ham_service.get_radio_state()
    )


@app.route('/api/ham/radio/start_tx', methods=["POST"])
def route_api_ham_radio_start_tx():
    ham_service.start_radio_tx()
    return "OK"


@app.route('/api/ham/radio/stop_tx', methods=["POST"])
def route_api_ham_radio_stop_tx():
    ham_service.stop_radio_tx()
    return "OK"


if __name__ == '__main__':
    app.run(
        port=8000,
        debug=True
    )
