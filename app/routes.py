# Routes route web urls to other components of your website
from flask import render_template, flash, redirect, url_for, request
from flask_login import current_user, login_user, logout_user, login_required
from werkzeug.urls import url_parse

from app import app
from app.models import User
from app.forms import ChatForm, LoginForm

@app.route('/')
@app.route('/index')
@login_required
def index():
    return render_template('index.html', title='Home')

@app.route('/')
@app.route('/chat', methods=['GET','POST'])
@login_required
def chat():
    form = ChatForm()
    if form.validate_on_submit():
        flash('User sent a msg!')
        return redirect(url_for('chat'))
    return render_template('chat.html', title='Chat', form=form)

@app.route('/')
@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        print(form.username.data, form.password.data)
        if user is None or not user.check_password(form.password.data):
            flash('Invalid Credentials')
            return redirect(url_for('login'))
        # TODO: Implement remember me!
        #login_user(user, remember=form.remember_me.data)
        login_user(user)
        next_page = request.args.get('next')
        if not next_page or url_parse(next_page).netloc != '':
            next_page = url_for('index')
        return redirect(next_page)
    return render_template('login.html', title='Sign In', form=form)

@app.route('/')
@app.route('/logout', methods=['GET', 'POST'])
def logout():
    logout_user()
    return redirect(url_for('index'))

