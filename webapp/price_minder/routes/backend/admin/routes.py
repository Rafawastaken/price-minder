from flask import Blueprint, render_template, flash, redirect, url_for
from flask_login import login_required, current_user
from .forms import ApiForm


##################### * Blueprint * #####################
admin = Blueprint('admin', __name__)


##################### * Helpers * #####################

# Function to check if user has permission to access admin panel
def check_permission():
    if current_user.level >= 2: return True
    return False


##################### * Main Admin * #####################

# Admin Index
@admin.route('/')
@login_required
def admin_index():
    title = "Price Minder - Admin Panel"
    if not check_permission():
        flash("You don't have permissions to view this area", "danger")
        return redirect(url_for('pages.index_pages'))
    
    return render_template('./backend/admin/index.html', title = title)


##################### * Admin Config * #####################

# Config Landing
@admin.route('/config')
@login_required
def admin_config():
    title = "Price Minder - Website Configurations"
    return render_template('./backend/admin/admin_config.html', title = title)


# API Config 
@admin.route('/config/api', methods = ['GET', 'POST'])
@login_required
def admin_api_config():
    title = "Price Minder - Api Configuration"
    form = ApiForm()

    return render_template('./backend/admin/api_config.html', title = title, form = form)