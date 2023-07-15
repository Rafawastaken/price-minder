from flask import Blueprint, request, url_for, render_template, flash, redirect
from flask_login import login_required, current_user

from .models import Game, Genre
from .forms import AddGameForm

##################### * Blueprint * #####################
games_management = Blueprint('games', __name__)


##################### * Helpers * #####################

# Function to check if user has permission to access admin panel
def check_permission():
    if current_user.level >= 2: return True
    return False

# Form errors flash
def flash_errors(errors):
    print(errors)
    for error in errors:
        for item in errors[error]:
            flash(f"{error.title()} - {item}", "danger")


##################### * Routes Games Management * #####################

# Index admin for game management
@games_management.route('/')
@login_required
def games_management_index():
    
    if not check_permission():
        flash("You don't have permissions to view this area", "danger")
        return redirect(url_for('pages.index_pages'))

    title = "Game List"
    games = Game.query.all()
    return render_template('./backend/games-management/games_list.html', title = title, games = games)


@games_management.route('/add-game', methods = ['POST', 'GET'])
@login_required
def games_management_add():
    if not check_permission():
        flash("You don't have permissions to view this area", "danger")
        return redirect(url_for('pages.index_pages'))

    title = "Add Games Forms"
    form = AddGameForm()

    if form.validate_on_submit():
        ...
    else:
        flash_errors(form.errors)

    return render_template('./backend/games-management/games_add.html', title = title, form = form)