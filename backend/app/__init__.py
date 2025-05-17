from flask import Flask
from .extensions import db, bcrypt, jwt
from .routes import register_blueprints
from .config import Config

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # Initialize extensions
    db.init_app(app)
    bcrypt.init_app(app)
    jwt.init_app(app)

    # Register blueprints
    register_blueprints(app)

    return app
