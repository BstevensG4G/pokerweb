import datetime
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Player(db.Model):
    __tablename__ = 'players'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(280), nullable=False)
    email = db.Column(db.String(280), nullable=False)
    password = db.Column(db.String(280), nullable=False)
    sex = db.Column(db.String(280), nullable=False)
    hand = db.Column(db.String(280), default="")
    bankroll = db.Column(db.Integer)
    table_stakes = db.Column(db.Integer)
    current_bet = db.Column(db.Integer)

    def __init__(self, name: str, email: str, password: str, sex: str):
        self.name = name
        self.email = email
        self.password = password
        self.sex = sex

    def serialize(self):
        return {
            'name': self.name,
            'email': self.email,
            'sex': self.sex
            
        }

playing = db.Table(
    'playing',
    db.Column(
        'player_id', db.Integer,
        db.ForeignKey('players.id'),
        primary_key=True
    ),

    db.Column(
        'table_id', db.Integer,
        db.ForeignKey('card_tables.id'),
        primary_key=True
    ),

    db.Column(
        'created_at', db.DateTime,
        default=datetime.datetime.utcnow,
        nullable=False
    )
)

class CardTable(db.Model):
    __tablename__ = 'card_tables'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    pot_amount = db.Column(db.Integer, nullable=False)
    min_stake = db.Column(db.Integer, nullable=False, default=5000)
    max_stake = db.Column(db.Integer, nullable=False, default=50000)
    hole_cards = db.Column(db.String(280), default="")
    game_type = db.Column(db.String(280), nullable=False)
    is_girls_only = db.Column(db.Boolean, nullable=False, default=False)

    def __init__(self, pot_amount: int, min_stake: int, max_stake: int, game_type: str):
        self.pot_amount = pot_amount
        self.min_stake = min_stake
        self.max_stake = max_stake
        self.game_type = game_type

    def serialize(self):
        return {
            'pot_amount': self.pot_amount,
            'min_stake': self.min_stake,
            'max_stake': self.max_stake,
            'game_type': self.game_type
            
        }

class Dealer(db.Model):
    __tablename__ = 'dealers'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(280), nullable=False, default="Gus")
    deck_id = db.Column(db.Integer, nullable=False)

    def __init__(self, name: str, deck_id: str):
        self.name = name
        self.deck_id = deck_id

    def serialize(self):
        return {
            'name': self.name,
            'deck_id': self.deck_id            
        }
