from flask import Blueprint, render_template, flash



##################### * Blueprint * #####################
admin = Blueprint('admin', __name__)


##################### * Main Admin * #####################

# Admin Index
@admin.route('/')
def admin_index():
    title = "Price Minder - Admin Panel"
    return render_template('./backend/admin/index.html', title = title)




