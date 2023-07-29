from flask import Blueprint, render_template, flash, redirect, url_for, request
from flask_login import login_required, current_user

from price_minder import db
from .forms import ApiForm
from .models import ApiKey


##################### * Blueprint * #####################
admin = Blueprint('admin', __name__)


##################### * Helpers * #####################

# Function to check if user has permission to access admin panel
def check_permission():
    if current_user.level >= 2: return True
    return False

# Function to flash errors in form submission
def flash_errors(errors):
    print(errors)
    for error in errors:
        for item in errors[error]:
            flash(f"{error.title()} - {item}", "danger")


##################### * Main Admin * #####################

# Admin Index
@admin.route('/')
@login_required
def admin_index():
    if not check_permission():
        flash("You don't have permissions to view this area", "danger")
        return redirect(url_for('pages.index_pages'))
    
    title = "Price Minder - Admin Panel"
    return render_template('./backend/admin/index.html', title = title)


##################### * Admin Config * #####################

# Config Landing
@admin.route('/config')
@login_required
def admin_config():
    if not check_permission():
        flash("You don't have permissions to view this area", "danger")
        return redirect(url_for('pages.index_pages'))
    title = "Price Minder - Website Configurations"
    return render_template('./backend/admin/admin_config.html', title = title)


# API Config 
@admin.route('/config/api', methods = ['GET', 'POST'])
@login_required
def admin_api_config():
    if not check_permission():
        flash("You don't have permissions to view this area", "danger")
        return redirect(url_for('pages.index_pages'))

    title = "Price Minder - Api Configuration"
    form = ApiForm()
    api_key = ApiKey.query.first()

    if form.validate_on_submit():
        if not api_key:
            api = ApiKey(key = form.key.data)
            db.session.add(api)
        else:
            api_key.key = form.key.data    
        db.session.commit()
        flash('API Key updated', "success")
        return redirect(url_for('admin.admin_config'))
    else:
        flash_errors(form.errors)

    return render_template('./backend/admin/api_config.html', title = title, form = form, api_key=api_key)