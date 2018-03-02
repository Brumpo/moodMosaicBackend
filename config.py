import os

from setup import basedir


class BaseConfig(object):
    SECRET_KEY = "SO_SECURE"
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'postgres://localhost/moodmosaic'#'postgresql+psycopg2://moodmosaic'#os.environ['DATABASE_URL']
    SQLALCHEMY_TRACK_MODIFICATIONS = True


class TestingConfig(object):
    """Development configuration."""
    TESTING = True
    DEBUG = True
    WTF_CSRF_ENABLED = False
    SQLALCHEMY_DATABASE_URI = 'psql:///:memory:'
    DEBUG_TB_ENABLED = True
    PRESERVE_CONTEXT_ON_EXCEPTION = False
