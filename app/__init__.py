from flask import Flask
from .config import Config
from extensions.db import db
from extensions.jwt import jwt
from flask_migrate import Migrate

# Initialize Migrate
migrate = Migrate()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # Initialize extensions
    db.init_app(app)
    jwt.init_app(app)
    migrate.init_app(app, db)

    # Import models so Alembic can detect
    from models import User
    from models import Delivery
    from models import Order
    from models import Restaurant
    from models import DeliveryBoy

    @app.route("/")
    def index():
        return "Delivery Management System is running !"

    return app
