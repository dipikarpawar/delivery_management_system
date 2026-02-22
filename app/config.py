import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    ENVIRONMENT = os.getenv('FLASK_ENV')
    SECRET_KEY = os.getenv('SECRET_KEY')
    JWT_SECRET_KEY = os.getenv('JWT_SECRET_KEY')
    DATABASE_URI = os.getenv('DATABASE_URI')

class DevelopmentConfig(Config):
    DEBUG = True

class ProductionConfig(Config):
    DEBUG = False