from flask import Flask
from .extensions import db, ma, migrate
from .routes.book_routes import book_bp
from .routes.publisher_routes import publisher_bp
from .routes.category_routes import category_bp
from config import Config

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # Initialize extensions
    db.init_app(app)
    ma.init_app(app)
    migrate.init_app(app, db)

    # Import models so Alembic detects them
    from . import models  # noqa: F401

    # Register blueprints
    app.register_blueprint(book_bp, url_prefix="/books")
    app.register_blueprint(publisher_bp, url_prefix="/publishers")
    app.register_blueprint(category_bp, url_prefix="/categories")

    return app