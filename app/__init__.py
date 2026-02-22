from flask import Flask
from app.extensions import db, jwt
from app.config import DevelopmentConfig

def create_app(config_class = DevelopmentConfig):
    app = Flask(__name__)
    app.config.from_object(config_class)

    # Initialize extensions
    db.init_app(app)
    jwt.init_app(app)

    return app
