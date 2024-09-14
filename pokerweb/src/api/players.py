from flask import Blueprint, jsonify, abort, request
import hashlib
import secrets

from ..models import Player, db

bp_players = Blueprint('players', __name__, url_prefix='/players')

def scramble(password: str):
    """Hash and salt the given password"""
    salt = secrets.token_hex(16)
    return hashlib.sha512((password + salt).encode('utf-8')).hexdigest()

@bp_players.route('', methods=['GET']) # decorator takes path and list of HTTP verbs
def index():
    players = Player.query.all() # ORM performs SELECT query
    result = []
    for player in players:
        result.append(player.serialize()) # build list of Tweets as dictionaries
    return jsonify(result) # return JSON response

@bp_players.route('/<int:id>', methods=['GET'])
def show(id: int):
    player = Player.query.get_or_404(id)
    return jsonify(player.serialize())

@bp_players.route('/<int:id>', methods=['DELETE'])
def delete(id: int):
    player = Player.query.get_or_404(id)
    try:
        db.session.delete(player) # prepare DELETE statement
        db.session.commit() # execute DELETE statement
        return jsonify(True)
    except:
        # something went wrong :(
        return jsonify(False)
    
@bp_players.route('', methods=['POST'])
def create():
    # req body must contain user_id and content
    if 'name' not in request.json or 'password' not in request.json:
        return abort(400)
    if len(request.json['name']) < 8 or len(request.json['password']) < 3:
        return abort(400)

    player = Player(
        name=request.json['name'],
        email=request.json['email'],
        password=scramble(request.json['password']),
        sex=request.json['sex'],
        bankroll=request.json['bankroll']
        )
    try:
        db.session.add(player) # prepare CREATE statement
        db.session.commit() # execute CREATE statement
        return jsonify(player.serialize())
    except:
        return (Exception)

@bp_players.route('/<int:id>', methods=['PATCH', 'PUT'])
def update(id: int):
    player = Player.query.get_or_404(id)
    if 'password' not in request.json or 'email' not in request.json:
        return abort(400)
    
    player.email=request.json['email']
    player.password=scramble(request.json['password'])
    if 'name' in request.json:
        player.name=request.json['name']
    if 'bankroll' in request.json:
        player.bankroll=request.json['bankroll']
    elif 'sex' in request.json:
        player.bankroll=request.json['sex']        
    
    try:
        db.session.add(player) # prepare Add statement
        db.session.commit() # execute Update statement
        return jsonify(True)
    except:
        # something went wrong :(
        return jsonify(False)