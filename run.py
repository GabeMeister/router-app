""" Run the app in debug mode """

# pylint: disable=C0103,C0111,C0413,C0412,C0411,C0330

from flask import Flask, render_template

app = Flask(__name__,
    static_url_path='/static',
    static_folder='frontend/dist/static',
    template_folder='frontend/dist')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/<path:path>')
def fallback(path):
    return render_template('index.html')

app.run(debug=True)
