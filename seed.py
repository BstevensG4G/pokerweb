import random
import string
import hashlib
import secrets
from faker import Faker
from pokerweb.src.models import Player, CardTable, playing, Dealer, db
from pokerweb import create_app

PLAYER_COUNT = 50
TABLE_COUNT = 25
PLAYING_COUNT = 12


def random_passhash():
    """Get hashed and salted password of length N | 8 <= N <= 15"""
    raw = ''.join(
        random.choices(
            string.ascii_letters + string.digits + '!@#$%&', # valid pw characters
            k=random.randint(8, 15) # length of pw
        )
    )

    salt = secrets.token_hex(16)

    return hashlib.sha512((raw + salt).encode('utf-8')).hexdigest()


def truncate_tables():
    """Delete all rows from database tables"""
    db.session.execute(playing.delete())
    CardTable.query.delete()
    Player.query.delete()
    Dealer.query.delete()
    db.session.commit()


def main():
    """Main driver function"""
    app = create_app()
    app.app_context().push()
    truncate_tables()
    fake = Faker()

    last_player = None  # save last player
    for _ in range(PLAYER_COUNT):
        last_player = Player(
            name=fake.unique.name().lower() + str(random.randint(1,150)),
            email=fake.unique.email().lower(),
            password=random_passhash(),
            sex="male"
        )
        db.session.add(last_player)

    # insert players
    db.session.commit()

    last_table = None  # save last table
    for _ in range(TABLE_COUNT):
        last_table = CardTable(
            pot_amount=random.randint(1,1500),
            game_type=fake.unique.name().lower(),

        )
        db.session.add(last_table)

    # insert tables
    db.session.commit()

    player_table_pairs = set()
    while len(player_table_pairs) < PLAYING_COUNT:

        candidate = (
            random.randint(last_player.id - PLAYER_COUNT + 1, last_player.id),
            random.randint(last_table.id - TABLE_COUNT + 1, last_table.id)
        )

        if candidate in player_table_pairs:
            continue  # pairs must be unique

        player_table_pairs.add(candidate)

    new_playing = [{"player_id": pair[0], "table_id": pair[1]} for pair in list(player_table_pairs)]
    insert_playing_query = playing.insert().values(new_playing)
    db.session.execute(insert_playing_query)

    # insert likes
    db.session.commit()


# run script
main()