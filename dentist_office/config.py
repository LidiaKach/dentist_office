
class Config(object):
    # Flask Settings
    DEBUG = False
    TESTING = False

    # SQLAlchemy settings
    SQLALCHEMY_DATABASE_URI = "postgresql://den:jw8s0F4@localhost/dentist"
    SQLALCHEMY_TRACK_MODIFICATIONS = True


class ProductionConfig(Config):
    pass


class DevelopmentConfig(Config):
    DEBUG = True

    SQLALCHEMY_DATABASE_URI = "postgresql://den:jw8s0F4@localhost/dentist"




class TestingConfig(Config):
    TESTING = True
    DEBUG = True

    SQLALCHEMY_DATABASE_URI = "postgresql://testUser:jw9s0F3@localhost/testdb"
