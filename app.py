from flask import Flask, render_template, url_for

app = Flask(
    __name__
)


@app.route('/')
def route_index():
    page_html = "<p>Please make a selection:</p>"
    for url_title, url_target in [
        # ('Home', url_for('route_index')),
        ('Test', url_for('route_test')),
        ('Control', url_for('route_control')),
        ('About', url_for('route_about')),
    ]:
        page_html += f"<p><a href='{url_target}'>{url_title}</a></p>"
    return render_template('simple_html.html',
                           site_title='Home',
                           page_html=page_html,
                           )


@app.route('/test')
def route_test():
    return render_template('simple_content.html',
                           site_title='Test',
                           page_content='Hello World!',
                           )


@app.route('/control')
def route_control():
    return render_template('simple_content.html',
                           site_title='Control',
                           page_content='Hello World!',
                           )


@app.route('/about')
def route_about():
    return render_template('simple_content.html',
                           site_title='About',
                           page_content='Hello World!',
                           )


if __name__ == '__main__':
    app.run(
        port=8000,
        debug=True
    )
