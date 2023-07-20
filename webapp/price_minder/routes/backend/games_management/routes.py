from flask import Blueprint, request, url_for, render_template, flash, redirect
from flask_login import login_required, current_user

from price_minder import db
from .models import Game, Genre
from .forms import AddGameForm, AddGenreForm

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

# index for games
@management.route('/games')
@login_required
def games_management_index():
    
    if not check_permission():
        flash("You don't have permissions to view this area", "danger")
        return redirect(url_for('pages.index_pages'))

    title = "Game List"
    games = Game.query.all()
    return render_template('./backend/games-management/games/games_list.html', title = title, games = games)

# add games
@management.route('/games/add-game', methods = ['POST', 'GET'])
@login_required
def games_management_add():
    if not check_permission():
        flash("You don't have permissions to view this area", "danger")
        return redirect(url_for('pages.index_pages'))

    title = "Add Games"
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

    return render_template('./backend/games-management/games/games_add.html', title = title, form = form)


##################### * Categories Management * #####################

# index genres
@management.route('/genres')
@login_required
def genres_management_index():
    if not check_permission():
        flash("You don't have permissions to view this area", "danger")
        return redirect(url_for('pages.index_pages'))

    title = "Genres List"
    genres = Genre.query.all()
    return render_template('./backend/games-management/genres/genres_list.html', title = title, genres = genres)

# add genre
@management.route('/genres/add-genre', methods=['POST', 'GET'])
@login_required
def genres_management_add():
    if not check_permission():
        flash("You don't have permissions to view this area", "danger")
        return redirect(url_for('pages.index_pages'))
    
    title = "Add Genre"
    form = AddGenreForm()

    if form.validate_on_submit():
        new_genre = Genre(name=form.name.data)
        db.session.add(new_genre)
        db.session.commit()
        flash(f"'{form.name.data}' added to Genres", "success")
        return redirect(url_for('games_management.genres_management_index'))
    else:
        flash_errors(form.errors)

    return render_template('./backend/games-management/genres/genres_add.html', title=title, form=form)

# edit genre
@management.route('/genres/edit/<int:id>', methods=['GET', 'POST'])
@login_required
def genres_management_edit(id):
    title = "Edit "
    return

# delete genre
@management.route('/genres/delete/<int:id>', methods=['POST', 'GET'])
@login_required
def genres_management_del(id):
    genre = Genre.query.get_or_404(id)
    
    db.session.delete(genre)
    db.session.commit()

    flash(f'Genre "{genre.name}" deleted', 'success')
    return redirect(url_for('games_management.genres_management_index'))