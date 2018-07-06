import os
PROJECT_DIR = os.path.abspath(__file__).rsplit('/',3)[0]

class Config(object):
    """Parent configuration class."""
    # DEBUG = False
    # CSRF_ENABLED = True
    # SECRET = os.getenv('SECRET', 'This is my secret')
    # SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL')
    # SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = 'p9Bv<3Eid9%$i04'
    MYSQL_USERNAME = 'root'
    MYSQL_PASSWORD = 'root'
    MYSQL_HOST = 'localhost'
    MYSQL_DB = 'testdb'
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:root@localhost/testdb'
    captcha_decoder_api_key = 'f28111ba3872d17dd27031ea40fc217e'


class DevelopmentConfig(Config):
    """Configurations for Development."""
    DEBUG = True

class TestingConfig(Config):
    """Configurations for Testing, with a separate test database."""
    TESTING = True
    #SQLALCHEMY_DATABASE_URI = 'postgresql://localhost/test_db'
    SQLALCHEMY_DATABASE_URI = 'sqlite:////' + PROJECT_DIR + '/test_db/polls.db'
    print('SQLALCHEMY_DATABASE_URI', SQLALCHEMY_DATABASE_URI)
    DEBUG = True

class StagingConfig(Config):
    """Configurations for Staging."""
    DEBUG = True

class ProductionConfig(Config):
    """Configurations for Production."""
    DEBUG = False
    TESTING = False

app_config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'staging': StagingConfig,
    'production': ProductionConfig,
}
