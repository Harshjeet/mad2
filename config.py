class Config(object):
    DEBUG = False
    TESTING = False
    
class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///grocery_database.db'
    SECRET_KEY = 'my_precious'
    SECURITY_PASSWORD_SALT = 'this is used for encrypting the password'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    WTF_CSRF_ENABLED = False # means it is used to protect the form
    SECURITY_TOKEN_AUTHENTICATION_HEADER = 'Authentication-key'
    