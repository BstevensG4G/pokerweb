import os
from flask import Flask
from flask_migrate import Migrate

from .config import Config
from .src.api.players import bp_players
from .src.api.card_tables import bp_card_tables
from .src.api.playing import bp_playing
from .src.api.dealers import bp_dealers
from .src.models import db


def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY=Config.SECRET_KEY,
        #SQLALCHEMY_DATABASE_URI='postgresql://postgres@pgdb:5432/pokerweb',
        #SQLALCHEMY_DATABASE_URI=Config.SQLITE3_DB,
        SQLALCHEMY_DATABASE_URI='sqlite:///pgdb.db',
        SQLALCHEMY_TRACK_MODIFICATIONS=False,
        SQLALCHEMY_ECHO=True
    )

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    from .src.models import db
    migrate = Migrate(app, db)
    db.init_app(app)

    #app.register_blueprint(players.bp)
    app.register_blueprint(bp_players)
    app.register_blueprint(bp_card_tables)
    app.register_blueprint(bp_playing)
    app.register_blueprint(bp_dealers)

    return app