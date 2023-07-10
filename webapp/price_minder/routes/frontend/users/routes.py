from flask import Blueprint, render_template, flash
from .models import User

##################### * Blueprint * #####################
users = Blueprint('users', __name__)


##################### * Routes * #####################

@users.route('/')
def users_index():
    return "users index"

##################### * Login System * #####################

# Register user
@users.route('/sign-up', methods = ['POST', 'GET'])
def sign_up():
    return render_template('./frontend/users/register.html')


# Login user
@users.route('/login', methods = ['POST', 'GET'])
def login():
    return "login"