import os

class Config(object):
    APP_TITLE = 'Blog of books'
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'very_secret_key!'
    API_ROOT_URL = 'http://localhost:5000/api'
    
