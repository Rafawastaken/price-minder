from flask import Blueprint, render_template, flash


##################### * Blueprint * #####################
pages = Blueprint('pages', __name__)


##################### * Frontend routes * #####################
@pages.route('/')
def index_pages():
    return render_template('./frontend/pages/index.html')