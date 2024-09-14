from flask import Blueprint, jsonify, abort, request
from ..models import CardTable, db

bp_card_tables = Blueprint('card_tables', __name__, url_prefix='/tables')

@bp_card_tables.route('', methods=['GET']) # decorator takes path and list of HTTP verbs
def index():
    tables = CardTable.query.all() # ORM performs SELECT query
    result = []
    for table in tables:
        result.append(table.serialize()) # build list of Tweets as dictionaries
    return jsonify(result) # return JSON response
    

@bp_card_tables.route('/<int:id>', methods=['GET'])
def show(id: int):
    table = CardTable.query.get_or_404(id)
    return jsonify(table.serialize())

@bp_card_tables.route('/<int:id>', methods=['DELETE'])
def delete(id: int):
    table = CardTable.query.get_or_404(id)
    try:
        db.session.delete(table) # prepare DELETE statement
        db.session.commit() # execute DELETE statement
        return jsonify(True)
    except:
        # something went wrong :(
        return jsonify(False)

@bp_card_tables.route('', methods=['POST'])
def create():
    # req body must contain game_type and content
    if 'game_type' not in request.json:
        return abort(400)

    table = CardTable(
        pot_amount=request.json['pot_amount'],
        min_stake=request.json['min_stake'],
        max_stake=request.json['max_stake'],
        game_type=request.json['game_type']
        )
    try:
        db.session.add(table) # prepare CREATE statement
        db.session.commit() # execute CREATE statement
        return jsonify(table.serialize())
    except:
        return (Exception)

@bp_card_tables.route('/<int:id>', methods=['PATCH', 'PUT'])
def update(id: int):
    table = CardTable.query.get_or_404(id)

    if 'pot_amount' in request.json:
        table.pot_amount=request.json['pot_amount']
    if 'min_stake' in request.json:
        table.min_stake=request.json['min_stake']
    if 'max_stake' in request.json:
        table.max_stake=request.json['max_stake']  
    if 'game_type' in request.json:
        table.game_type=request.json['game_type']            
    
    try:
        db.session.add(table) # prepare Add statement
        db.session.commit() # execute Update statement
        return jsonify(True)
    except:
        # something went wrong :(
        return jsonify(False)