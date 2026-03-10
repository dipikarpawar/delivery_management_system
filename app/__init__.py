from flask import Flask
from app.extensions import db, jwt, migrate
from app.config import DevelopmentConfig, ProductionConfig
import os

def create_app():
    app = Flask(__name__)
    
    if os.getenv('FLASK_ENV') == 'production':
        app.config.from_object(ProductionConfig)
    else:
        app.config.from_object(DevelopmentConfig)

    # Initialize extensions
    db.init_app(app)
    migrate.init_app(app, db)
    jwt.init_app(app)

    return app