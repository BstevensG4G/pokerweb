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
    