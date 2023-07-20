from price_minder import db

# class for games in database
class Game(db.Model):
    # Meta
    id = db.Column(db.Integer, primary_key=True)
    steam_id = db.Column(db.Integer, unique = True, nullable = False)
    name = db.Column(db.String(200), unique = True, nullable = False)
    release_date = db.Column(db.String(30), unique = True, nullable = False)
    type_product = db.Column(db.String(30), unique = True, nullable = False)
    description = db.Column(db.String(1000), unique = True, nullable = False)

    # Genres
    genre_id = db.Column(db.Integer, db.ForeignKey('genre.id'), nullable = False)
    genre = db.relationship('Genre', backref=db.backref('genres', lazy = True))

    # Image
    header_img = db.Column(db.String(300), unique = True, nullable = False)
    capsule_img = db.Column(db.String(300), unique = True, nullable = False)
    capsule_imgv5 = db.Column(db.String(300), unique = True, nullable = False)

    # Price
    price = db.Column(db.String(7), unique = True, nullable = False)
    on_sale = db.Column(db.String(300), unique = True, nullable = False)
    discount_price = db.Column(db.String(300), unique = True, nullable = False)
    discount_percent =  db.Column(db.String(300), unique = True, nullable = False)
    

# class for genres in database
class Genre(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), unique = True, nullable = False)