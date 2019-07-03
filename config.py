class Config:
    SECRET_KEY = 's0meSecretKey'

class Development(Config):
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:123@127.0.0.1:5432/june_payroll_system'
    DEBUG = True

class Production(Config):
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:123@127.0.0.1:5432/june_payroll_system'
    DEBUG = False