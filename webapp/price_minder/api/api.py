from flask import Blueprint, session
from flask_restful import Resource, reqparse, abort, marshal_with, fields
from price_minder import db, bcrypt, auth

# Database models
from price_minder.routes.backend.games_management.models import Game


##################### * Blueprint * #####################
api_bp = Blueprint('api', __name__)


##################### * Auth Verification * #####################

@auth.verify_password
def verify(access_name, access_key):
    ...


########################## * Games List * #####################
game_list_resource_fields = {}
#teste git creds


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
    @marshal_with(game_details_resource_fields)
    def get(self, steam_id):
        game = Game.query.filter_by(steam_id=steam_id).first()

        if game is None: return {"message": "Game not found"}, 404

        return game, 200