from datetime import datetime
from app import db

class User(db.Model):
    """ Model to store user informations """
    def __repr__(self):
        return '<User {}>'.format(self.username)

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    sent_msgs = db.relationship('Msg', backref='Sender', lazy='dynamic',
                                foreign_keys='Msg.from_id')
    received_msgs = db.relationship('Msg', backref='Receiver', lazy='dynamic',
                                   foreign_keys='Msg.to_id')

class Msg(db.Model):
    """ Model to store messages """
    def __repr__(self):
        return '<Msg id #{}>'.format(self.id)

    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(32))
    from_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    to_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
