from flask import Blueprint, request, url_for, render_template
from flask_login import login_required, current_user
from .models import Game, Genre

##################### * Blueprint * #####################
games_management = Blueprint('games', __name__)


##################### * Helpers * #####################

# Function to check if user has permission to access admin panel
def check_permission():
    if current_user.level >= 2: return True
    return False


##################### * Routes Games Management * #####################

# Index admin for game management
@games_management.route('/')
@login_required
def games_management_index():
    title = "Game List"
    games = Game.query.all()
    return render_template('./backend/games-management/games_list.html', games = games)


@games_management.route('/add-game', methods = ['POST', 'GET'])
@login_required
def games_management_add():
    ...