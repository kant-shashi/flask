import os


class Config(object):
    DEBUG = True
    TESTING = False
    APP_ROOT = os.path.dirname(os.path.realpath(__file__))
    DATABASE = os.path.join(APP_ROOT, 'flask.db')


class ProductionConfig(Config):
    DEBUG = False


class DevelopmentConfig(Config):
    SECRET_KEY = 'development key'
    USERNAME = 'admin'
    PASSWORD = 'default'


class TestingConfig(Config):
    TESTING = True
