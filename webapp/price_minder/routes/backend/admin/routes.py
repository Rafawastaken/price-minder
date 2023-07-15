from flask import Blueprint, render_template, flash, redirect, url_for
from flask_login import login_required, current_user



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




