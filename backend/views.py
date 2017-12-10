""" Define the views """

from backend import app
from flask import render_template

@app.route('/')
@app.route('/index')
def index():
    print 'here'
    print 'template folder: '
    print app.template_folder
    return render_template('index.html')
