from price_minder import db, login_manager
from flask_login import UserMixin

from ...backend.games_management.models import Game

# Login Manager
@login_manager.user_loader
def user_loader(user_id):
    return User.query.get(user_id)

# Users models
class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(30), unique = True, nullable = False)
    email = db.Column(db.String(120), unique = True, nullable = False)
    password = db.Column(db.String(180), unique = False, nullable = False)

    # # ! Games Liked 
    # liked_games_id = db.Column(db.Integer, db.ForeignKey('game.id'), nullable = True)
    # liked_games = db.relationship('Game', backref = db.backref('games'), lazy=True)

    # level parameter differentiates the user types (user, admin)
    level = db.Column(db.Integer, nullable = False, unique = False)