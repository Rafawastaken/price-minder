from price_minder import app, db, bcrypt

from flask import Blueprint, render_template, flash, redirect, url_for, request
from flask_login import login_user, logout_user

from .models import User
from .forms import SignupForm, LoginForm

##################### * Blueprint * #####################

users = Blueprint('users', __name__)


##################### * Helper Functions * #####################

# Flash errors
def flash_errors(errors):
    print(errors)
    for error in errors:
        for item in errors[error]:
            flash(f"{error.title()} - {item}", "danger")

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

        login_user(new_user)
        flash(f"Welcome to Price-Minder {form.username.data}!", "success")
        return redirect(url_for(url_for('pages.index_pages')))
    else:
        flash_errors(form.errors)

    return render_template('./frontend/users/register.html', form = form, title = title)


# Login user
@users.route('/login', methods = ['POST', 'GET'])
def login():
    form = LoginForm()
    title = "Price Minder - Login"

    if form.validate_on_submit():
        # Query user 
        user = User.query.filter_by(email = form.email.data).first()

        # Check if user and password match
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user)
            flash(f'Welcome back: {user.username.title()}', "success")
            next = request.args.get('next')
            return redirect(next or url_for('pages.index_pages'))
        
        else: flash("Incorrect Email or Password", "danger")

    # Flash form errors
    else: flash_errors(form.errors)
    return render_template('./frontend/users/login.html', form = form, title = title)


# Logout users
@users.route('/logout', methods = ['POST'])
def logout():
    logout_user()
    flash('We will miss you...', "success")
    return redirect(url_for('pages.index_pages'))