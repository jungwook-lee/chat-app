# Routes route web urls to other components of your website
from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'User A'}
    msgs = [
        {'author': 'User B',
         'content': 'Hello There!'},
        {'author': 'User C',
         'content': 'It\'s treason then.'}
    ]
    return render_template('index.html', title='Home', user=user, msgs=msgs)
