class Config(object):
    DEBUG = False
    TESTING = False
    SQLALCHEMY_DATABASE_URI = 'sqlite:///db.sqlite'
    SESSION_COOKIE_SECURE = True


class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'sqlite:///db.sqlite'
    pass


class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///db.sqlite'
    SESSION_COOKIE_SECURE = False


class TestingConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///db.sqlite'
    SESSION_COOKIE_SECURE = False
