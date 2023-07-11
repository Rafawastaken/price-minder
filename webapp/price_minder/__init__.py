from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from flask_bcrypt import Bcrypt


app = Flask(__name__)
db = SQLAlchemy()


with app.app_context():
    # Load configs
    app.config.from_pyfile("config.py")

    # Init database
    db = SQLAlchemy(app)

    # Bcrypt
    bcrypt = Bcrypt(app)

    # Login Mananger
    login_manager = LoginManager()
    login_manager.init_app(app)
    login_manager.login_view = 'users.login'
    login_manager.login_message_category = 'danger'
    login_manager.needs_refresh_message_category ='danger'
    login_manager.login_message = u'Need to login to view this page'

    # Flask database migrations
    migrate = Migrate(app, db)

    # Import Routes
    from .routes.backend.admin.routes import admin
    from .routes.frontend.users.routes import users
    from .routes.frontend.pages.routes import pages

    # Register blueprints
    app.register_blueprint(users, url_prefix = '/')
    app.register_blueprint(admin, url_prefix = '/admin')
    app.register_blueprint(pages, url_prefix = '/')