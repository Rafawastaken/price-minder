from flask import Blueprint, render_template, url_for, redirect, flash
from flask_login import current_user, login_required

from price_minder import app, db


from ...frontend.users.models import User

##################### * Blueprint * #####################
admin_users = Blueprint("admin_users", __name__)


##################### * Helpers * #####################

# Function to check if user has permission to access admin panel
def check_permission():
    if current_user.level >= 2: return True
    return False


##################### * Users Management * #####################
@admin_users.route('/')
@login_required
def users():
    title = "Users Registered"

    if not check_permission():
        flash("You don't have permissions to view this area", "danger")
        return redirect(url_for('pages.index_pages'))
    
    users = User.query.all()
    return render_template('./backend/user-management/users_list.html', title = title, users = users)


@admin_users.route('/promote/<int:id>', methods = ['POST'])
@login_required
def promote(id):
    if not check_permission():
        flash("You don't have permissions to view this area", "danger")
        return redirect(url_for('pages.index_pages'))

    user = User.query.filter_by(id = id).first()
    if not user:
        flash("Couldn't find user to promote", "danger")
    else:
        user.level = 2
        db.session.commit()
        flash(f'{user.username} was promoted to level: 2', "success")
    return redirect(url_for('admin_users.users'))