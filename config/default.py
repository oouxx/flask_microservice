import os


class Config(object):
    # BASEDIR = os.path.abspath(os.path.dirname(__file__))
    DEBUG = True
    TESTING = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = os.environ.get(
        'DATABASE_URL') or 'mysql+pymysql://root:wxx1512@localhost:3306/learning_flask'
    # SQLALCHEMY_DATABASE_URI = 'mysql'
    SECRET_KEY = 'you-will-never-guess'
