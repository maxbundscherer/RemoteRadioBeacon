from flask import Flask, render_template, url_for, jsonify, request

from backend.TestService import TestService

test_service: TestService = TestService()

app = Flask(
    __name__
)


@app.route('/')
def route_index():
    page_html = "<p>Please make a selection:</p><ul>"
    for url_title, url_target in [
        ('Control', url_for('route_control')),
        ('Test', url_for('route_test')),
        ('About', url_for('route_about')),
    ]:
        page_html += f'<li><a href="{url_target}">{url_title}</a></li>'
    page_html += "</ul>"
    return render_template('simple_html.html',
                           site_title='Home',
                           page_html=page_html,
                           )


@app.route('/control')
def route_control():
    return render_template('simple_content.html',
                           site_title='Control',
                           page_content='Hello World!',
                           )


@app.route('/test', methods=['GET', 'POST'])
def route_test():
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

    return render_template('test.html',
                           site_title='Test',
                           )


@app.route('/about')
def route_about():
    return render_template('simple_content.html',
                           site_title='About',
                           page_content='Hello World!',
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
