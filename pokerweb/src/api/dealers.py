from flask import Blueprint, jsonify
from ..models import Dealer, db

bp_dealers = Blueprint('dealers', __name__, url_prefix='/dealers')

@bp_dealers.route('', methods=['GET']) # decorator takes path and list of HTTP verbs
def index():
    dealers = Dealer.query.all() # ORM performs SELECT query
    result = []
    for dealer in dealers:
        result.append(dealer.serialize()) # build list of Tweets as dictionaries
    return jsonify(result) # return JSON response