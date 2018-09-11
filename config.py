import os

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'this-is-a-very-secret-key'