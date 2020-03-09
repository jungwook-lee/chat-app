# Routes route web urls to other components of your website
from flask import render_template, flash, redirect, url_for
from app import app

from app.forms import ChatForm

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'User A'}
    return render_template('index.html', title='Home', user=user)

@app.route('/')
@app.route('/chat', methods=['GET','POST'])
def chat():
    user = {'username': 'User A'}
    msgs = [
        {'author': 'User B',
         'content': 'Hello There!'},
        {'author': 'User C',
         'content': 'It\'s treason then.'}
    ]
    form = ChatForm()
    if form.validate_on_submit():
        flash('User sent a msg!')
        return redirect(url_for('chat'))
    return render_template('chat.html', title='Chat', user=user,  msgs=msgs,
                           form=form)
