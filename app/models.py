from datetime import datetime
from app import db, login
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin

class User(UserMixin, db.Model):
    """ Model to store user informations 

    UserMixin implements the following properties, functions:
        - is_authenticated
        - is_active
        - is_anonymous
        - get_id()
    """
    def __repr__(self):
        return '<User {}>'.format(self.username)

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    sent_msgs = db.relationship('Msg', backref='Sender', lazy='dynamic',
                                foreign_keys='Msg.from_id')
    received_msgs = db.relationship('Msg', backref='Receiver', lazy='dynamic',
                                   foreign_keys='Msg.to_id')

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

class Msg(db.Model):
    """ Model to store messages """
    def __repr__(self):
        return '<Msg id #{}>'.format(self.id)

    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(32))
    from_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    to_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)

# Loads the user into the current session
@login.user_loader
def load_user(id):
    return User.query.get(int(id))
