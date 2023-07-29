from price_minder import db

# class for games in database
class ApiKey(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    key = db.Column(db.String(40), unique = True, nullable = False)