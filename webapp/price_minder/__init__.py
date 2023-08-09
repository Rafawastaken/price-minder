from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from flask_bcrypt import Bcrypt
from flask_restful import Api
from flask_httpauth import HTTPBasicAuth

app = Flask(__name__)
db = SQLAlchemy()


with app.app_context():
    # Load configs
    app.config.from_pyfile("config.py")

    # Init database
    db = SQLAlchemy(app)

    # Bcrypt
    bcrypt = Bcrypt(app)

    # Http auth
    auth = HTTPBasicAuth()

    # Login Mananger
    login_manager = LoginManager()
    login_manager.init_app(app)
    login_manager.login_view = 'users.login'
    login_manager.login_message_category = 'danger'
    login_manager.needs_refresh_message_category ='danger'
    login_manager.login_message = u'Need to login to view this page'

    # Flask database migrations
    migrate = Migrate(app, db)

    # Backend Routes
    from .routes.backend.admin.routes import admin
    from .routes.backend.user_management.routes import admin_users
    from .routes.backend.games_management.routes import management

    # Frontend Routes
    from .routes.frontend.users.routes import users
    from .routes.frontend.pages.routes import pages

    # Api
    from .api.api import api_bp

    # Backend blueprints
    app.register_blueprint(admin, url_prefix = '/admin')
    app.register_blueprint(management, url_prefix = '/admin/management')
    app.register_blueprint(admin_users, url_prefix = '/admin/users')

    # Frontend
    app.register_blueprint(users, url_prefix = '/')
    app.register_blueprint(pages, url_prefix = '/')

    # Api Restful
    api = Api(api_bp)

    app.register_blueprint(api_bp) # Api blueprin

    # Api Endpoints
    from .api.api import GameDetails
    from .api.api import GameList

    api.add_resource(GameDetails, "/api/game_details/<int:steam_id>")
    api.add_resource(GameList, "/api/game_list")
