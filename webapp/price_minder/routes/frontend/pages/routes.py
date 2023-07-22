from flask import Blueprint, render_template, flash

# models
from ...backend.games_management.models import Game, Genre


##################### * Blueprint * #####################
pages = Blueprint('pages', __name__)


##################### * Frontend routes * #####################
@pages.route('/')
def index_pages():
    title = "Price Minder"
    games = Game.query.all()
    return render_template('./frontend/pages/index.html', title=title, games=games)