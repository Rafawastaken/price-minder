from flask import Blueprint, request, url_for, render_template, flash, redirect
from flask_login import login_required, current_user

from .models import Game, Genre
from .forms import AddGameForm

##################### * Blueprint * #####################
management = Blueprint('games_management', __name__)


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


##################### * Games Management * #####################

# Index admin for game management
@management.route('/games')
@login_required
def games_management_index():
    
    if not check_permission():
        flash("You don't have permissions to view this area", "danger")
        return redirect(url_for('pages.index_pages'))

    title = "Game List"
    games = Game.query.all()
    return render_template('./backend/games-management/games_list.html', title = title, games = games)


@management.route('/games/add-game', methods = ['POST', 'GET'])
@login_required
def games_management_add():
    if not check_permission():
        flash("You don't have permissions to view this area", "danger")
        return redirect(url_for('pages.index_pages'))

    title = "Add Games Forms"
    form = AddGameForm()


    # ! Falta adicionar generos

    if form.validate_on_submit():
        # Meta
        steam_id = form.steam_id.data
        name = form.name.data
        release_date = form.release_date.data
        product_type = form.product_type.data
        description = form.description.data

        # Images
        link_header = form.link_header.data
        capsule_image = form.capsule_image.data
        capsule_imagev5 = form.capsule_imagev5.data

        # Prices
        price = form.price.data
        on_sale = form.on_sale.data
        discout_price = form.discount_price.data

        

        return "form sent"
    else:
        flash_errors(form.errors)

    return render_template('./backend/games-management/games_add.html', title = title, form = form)


##################### * Categories Management * #####################
@management.route('/genres')
@login_required
def categories_list():
    if not check_permission():
        flash("You don't have permissions to view this area", "danger")
        return redirect(url_for('pages.index_pages'))

    title = "Genres List"

    return render_template('./backend/games-management/games_list.html', title = title)