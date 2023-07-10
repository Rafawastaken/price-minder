from flask import Blueprint, render_template, flash
from .models import User
from .forms import SignupForm

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
    form = SignupForm()
    
    return render_template('./frontend/users/register.html', form = form)


# Login user
@users.route('/login', methods = ['POST', 'GET'])
def login():
    return "login"