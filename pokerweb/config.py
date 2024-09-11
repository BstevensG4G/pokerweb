import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    SQLITE3_DB = 'sqlite:///' + os.path.join(basedir, 'app.sqlite')