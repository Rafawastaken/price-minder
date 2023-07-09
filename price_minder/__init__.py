from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


app = Flask(__name__)
db = SQLAlchemy()


with app.app_context():
    # Load configs
    app.config.from_pyfile("config.py")

    # Init database
    db.init_app(app)

    # Flask database migrations
    migrate = Migrate(app, db)

    # Import Routes
    from .routes.admin.routes import admin

    # Register blueprints
    app.register_blueprint(admin, url_prefix = '/admin')
    