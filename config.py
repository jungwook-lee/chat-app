import os
basedir = os.path.abspath(os.path.dirname(__file__))

# Insert configurations here
class Config(object):
    # useful for generating security tokens
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'debugging-key'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
            'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
