from os import environ, path
import os

class Config:
    
    SECRET_KEY = os.urandom(70)#environ.get('SECRET_KEY')
    TEMPLATES_FOLDER = 'templates'
    STATIC_FOLDER = 'static'
    MODELS_FOLDER = 'models'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///src/database/data.db' #Connection string of my app's database
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class ConfigDevelopment(Config):
    
    FLASK_ENV = 'development'
    DEBUG = True
    TESTING = True
    
    """
    SQLITE_HOST = 'localhost'
    SQLITE_USER = 'root'
    SQLITE_PASSWORD = '123456'
    SQLITE_DB = 'flask_login'"""


config={
    'development': ConfigDevelopment
}
