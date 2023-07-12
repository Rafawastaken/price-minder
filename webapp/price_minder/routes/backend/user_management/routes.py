from flask import Blueprint, render_template, url_for, redirect
from price_minder import app, db
from ...frontend.users.models import User

##################### * Blueprint * #####################
admin_users = Blueprint("admin_users", __name__)


##################### * Users Management * #####################
@admin_users.route('/')
def users():
    title = "Users Registered"
    users = User.query.all()
    return render_template('./backend/user-management/users_list.html', title = title, users = users)