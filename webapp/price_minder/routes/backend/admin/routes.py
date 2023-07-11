from flask import Blueprint, render_template, flash



##################### * Blueprint * #####################
admin = Blueprint('admin', __name__)


##################### * Main Admin * #####################

# Admin Index
@admin.route('/')
def admin_index():
    title = "Price Minder Admin Panel"

    flash('success message', "success")
    flash('danger message', "danger")
    flash('warning message', "warning")
    return render_template('./backend/admin/index.html', title = title)




