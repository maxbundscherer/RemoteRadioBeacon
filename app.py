from flask import Flask, render_template

app = Flask(
    __name__,
)


@app.route('/')
def route_index():
    return render_template('simple_content.html',
                           site_title='Home',
                           page_content='tbd',
                           )


if __name__ == '__main__':
    app.run()
