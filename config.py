# This operates as a go-between for our app and either the servers we're hosting 
# on (if we deploy it to the internet), or to talk to our computer and interface 
# between our app and the command line or terminal (depending on if you're on Mac 
# or Windows).

import os

from dotenv import load_dotenv
basedir = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(basedir, '.env'))


class Config():
	'''
	Set config variables for the flask app
    using Environment variables where available.
    Otherwise create the config variable if not done already
    '''

SUPERBLOOM_APP = os.getenv('SUPERBLOOM_APP')
SUPERBLOOM_ENV = os.getenv('SUPERBLOOM_ENV')
SECRET_KEY = os.environ.get('SECRET_KEY')

SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URI') or 'sqlite:///' + os.path.join(basedir, 'app.db')
SQLALCHEMY_TRACK_NOTIFICAITONS = False