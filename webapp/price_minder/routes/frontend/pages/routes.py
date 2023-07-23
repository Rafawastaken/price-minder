from flask import Blueprint, render_template, flash, request

# models
from ...backend.games_management.models import Game, Genre


##################### * Blueprint * #####################

pages = Blueprint('pages', __name__)


##################### * Frontend routes * #####################
@pages.route('/')
def index_pages():
    title = "Price Minder"
    page = request.args.get('page', 1, type=int)
    games = Game.query.paginate(page=page, per_page=3, error_out=False)
    genres = Genre.query.all()
    return render_template('./frontend/pages/index.html', title=title, games=games, genres=genres)