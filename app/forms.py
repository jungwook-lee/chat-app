from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

class ChatForm(FlaskForm):
    text_field = StringField('Message', validators=[DataRequired()])
    submit = SubmitField('Send')

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = StringField('Password', validators=[DataRequired()])
    submit = SubmitField('Send')
