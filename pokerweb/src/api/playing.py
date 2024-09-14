from flask import Blueprint, jsonify
from ..models import Playing, db

bp_playing = Blueprint('playing', __name__, url_prefix='/playing')

@bp_playing.route('', methods=['GET']) # decorator takes path and list of HTTP verbs
def index():
    playing = Playing.query.all() # ORM performs SELECT query
    result = []
    for play in playing:
        result.append(play.serialize()) # build list of Tweets as dictionaries
    return jsonify(result) # return JSON response