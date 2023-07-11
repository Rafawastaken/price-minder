from price_minder import app, db, bcrypt
from flask import Blueprint, render_template, flash, redirect, url_for
from .models import User
from .forms import SignupForm

##################### * Blueprint * #####################

users = Blueprint('users', __name__)


##################### * Login System * #####################

# Register user
@users.route('/sign-up', methods = ['POST', 'GET'])
def sign_up():
    form = SignupForm()
    title = "Price Minder - Sign Up"

    if form.validate_on_submit():
        password_hash = bcrypt.generate_password_hash(form.password.data)
        new_user = User(username = form.username.data,
                        email = form.email.data,
                        password = password_hash,
                        level = 1)
        db.session.add(new_user)
        db.session.commit()

        flash(f"Welcome to Price-Minder {form.username.data}!", "success")
        return redirect(url_for("users.sign_up"))
    return render_template('./frontend/users/register.html', form = form, title = title)


# Login user
@users.route('/login', methods = ['POST', 'GET'])
def login():
    return "login"