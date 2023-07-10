from flask import Blueprint, render_template, flash



##################### * Blueprint * #####################
admin = Blueprint('admin', __name__)


##################### * Main Admin * #####################

# Admin Index
@admin.route('/')
def admin_index():
    flash('This is a success message', 'success')
    flash('This is an error message', 'danger')
    flash('This is a warning message', 'warning')
    return render_template('./backend/admin/index.html')




