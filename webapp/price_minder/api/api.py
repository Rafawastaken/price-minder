from flask import Blueprint, session, request
from flask_restful import Resource, reqparse, abort, marshal_with, fields
from price_minder import db, bcrypt, auth

from ..routes.backend.admin.models import ApiKey

# Database models
from price_minder.routes.backend.games_management.models import Game


##################### * Blueprint * #####################
api_bp = Blueprint('api', __name__)


##################### * Auth Verification * #####################

@auth.verify_password
def verify(username, password):
    # Check if access key matches the key in db
    api_key = ApiKey.query.first()
    if username == '' and password == api_key.key:
        return True
    return False



########################## * Games List * #####################
game_list_resource_fields = {
    'id': fields.Integer,
    'steam_id': fields.Integer,
    'name': fields.String,
    'release_date': fields.String,
    'type_product': fields.String,
    'description': fields.String,
    'genre_id': fields.Integer,
    'header_img': fields.String,
    'capsule_img': fields.String,
    'capsule_imgv5': fields.String,
    'price': fields.String,
    'on_sale': fields.String,
    'discount_price': fields.String,
    'discount_percent': fields.String,
}


class GameList(Resource):
    # Get games 
    @auth.login_required
    @marshal_with(game_list_resource_fields)
    def get(self):
        games = Game.query.all()
        return games

    # Post new game
    @auth.login_required
    @marshal_with(game_list_resource_fields)
    def post(self):
        data = request.json
        new_game = Game(
            steam_id=data['steam_id'],
            name=data['name'],
            release_date=data['release_date'],
            type_product=data['type_product'],
            description=data['description'],
            genre_id=data['genre_id'],
            header_img=data['header_img'],
            capsule_img=data['capsule_img'],
            capsule_imgv5=data['capsule_imgv5'],
            price=data['price'],
            on_sale=data['on_sale'],
            discount_price=data['discount_price'],
            discount_percent=data['discount_percent']
        )
        db.session.add(new_game)
        db.session.commit()
        return new_game, 201


########################## * Game Details * #####################

game_details_resource_fields = {
    "steam_id": fields.Integer,
    "name": fields.String,
    "release_date": fields.String,
    "type_product": fields.String,
    "description": fields.String,
    "genre_id": fields.Integer,
    "header_img": fields.String,
    "capsule_img": fields.String,
    "capsule_imgv5": fields.String,
    "price": fields.String,
    "on_sale": fields.Boolean,
    "discount_price":fields.String,
    "discount_percent": fields.String
}

class GameDetails(Resource):
    @auth.login_required
    @marshal_with(game_details_resource_fields)
    def get(self, steam_id):
        game = Game.query.filter_by(steam_id=steam_id).first()
        if game is None: return {"message": "Game not found"}, 404
        return game, 200