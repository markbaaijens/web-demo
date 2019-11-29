import os

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'very secret key!'
    API_ROOT_URL = 'http://localhost:5000'
    
