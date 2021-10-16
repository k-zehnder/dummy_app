# FLASK_SECRET_KEY = os.environ.get("FLASK_SECRET_KEY", "default_key")
# env, default
# just like counts.get() from chuck!

import os
from dotenv import load_dotenv

basedir = os.path.abspath(os.path.dirname(__file__))
#NOTE: 
load_dotenv(os.path.join(basedir, '.env'))
# try not to use because needed on heroku and shows creds security risk?

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    SQLALCHEMY_DATABASE_URI = os.environ.get('SQLALCHEMY_DATABASE_URI', '')
    #.replace(
    #     'postgres://', 'postgresql://') or \
    #     'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False