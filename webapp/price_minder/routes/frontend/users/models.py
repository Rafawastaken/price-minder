from price_minder import db, login_manager
from flask_login import UserMixin


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

    # level parameter differentiates the different user types (user, admin)
    level = db.Column(db.Integer, nullable = False, unique = False, default = 0)