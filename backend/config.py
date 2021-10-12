import os

class Config(object):
    SECRET_KEY=os.environ.get('FLASK_SECRET')
    CLIENT_ID=os.environ.get('FLASK_CLIENT_ID')
