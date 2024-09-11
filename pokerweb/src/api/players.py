from flask import Blueprint, jsonify
from ..models import Player, db

bp_players = Blueprint('players', __name__, url_prefix='/players')

@bp_players.route('', methods=['GET']) # decorator takes path and list of HTTP verbs
def index():
    players = Player.query.all() # ORM performs SELECT query
    result = []
    for player in players:
        result.append(player.serialize()) # build list of Tweets as dictionaries
    return jsonify(result) # return JSON response
