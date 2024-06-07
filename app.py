from flask import Flask, render_template, url_for, jsonify, request

from backend.HamService import HamService
from backend.TestService import TestService

test_service: TestService = TestService()
ham_service: HamService = HamService()

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
    return render_template('simple_html.html',
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
                           site_title='Test-UI',
                           page_test_int=test_service.get_test_int(),
                           page_test_description=test_service.get_test_description(),
                           )


@app.route('/about')
def route_about():
    return render_template('simple_content.html',
                           site_title='About',
                           page_content='73 de DD7MB',
                           )


@app.route('/api/test')
def route_api_test():
    return jsonify(
        test_service.get_test_item()
    )


if __name__ == '__main__':
    app.run(
        port=8000,
        debug=True
    )
