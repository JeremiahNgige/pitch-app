import os
class Config:
    '''
    general configuration parent class
    '''
    #email configurations
    MAIL_SERVER ='smtp.googlemail.com'
    MAIL_PORT =587
    MAIL_USE_TLS =True
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
    SQLALCHEMY_DATABASE_URI =os.environ.get('DATABASE_URL')
    SECRET_KEY = os.environ.get('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI ='postgres+psycopg2://kmocrtyoqsvyvx:5bcedc5a205221386efa5cd29f4c605f19bb001e182c2dbadc217a096865e454@ec2-3-224-97-209.compute-1.amazonaws.com:5432/d816a7i050f40n'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    UPLOADED_PHOTOS_DEST ='app/static/photos'
class ProdConfig(Config):
    '''
    production configuration subclass
    Args:
        Config: The general configuration class with the the general configuration settings
    '''
    SQLALCHEMY_DATABASE_URI ='postgres+psycopg2://kmocrtyoqsvyvx:5bcedc5a205221386efa5cd29f4c605f19bb001e182c2dbadc217a096865e454@ec2-3-224-97-209.compute-1.amazonaws.com:5432/d816a7i050f40n'
class DevConfig(Config):
    '''
    development configuration subclass
    Args:
        Config: The general configuration class with the the general configuration settings
    '''
    DEBUG = True
    
config_options = {
    'development':DevConfig,
    'production': ProdConfig
}
    