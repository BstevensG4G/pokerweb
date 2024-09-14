FORMAT: 1A

## - PokerWeb API

an online multi-player poker website below is a description of the endpoints

### GET /tables

returns a list of current poker tables

# Group Players

## Players [/players]

### Retrieve List of Players [GET]

    + Response 200 (application/json)
        + Attributes [(object), (object)]
            + id 1 (integer, auto-incremented, unique)
            + name (string, required)
            + email (string, required)
            + bankroll (integer, default=0)
            + hand(string, default="")
            + table_stakes (integer, default=0)
            + current_bet (integer, default=0)
        + Body
            `[{
                "bankroll": null,
                "current_bet": null,
                "email": "tina67@example.com",
                "hand": "",
                "id": 1,
                "name": "angela schroeder94",
                "sex": "male",
                "table_stakes": null
            },
            {
                "bankroll": null,
                "current_bet": null,
                "email": "ahicks@example.net",
                "hand": "",
                "id": 2,
                "name": "sherry ferguson102",
                "sex": "male",
                "table_stakes": null
            }]`

### Retrieve a single Player [GET]

    Returns a single JSON object

    + Response 200 (application/json)
        + Body
            {
            "bankroll": null,
            "current_bet": null,
            "email": "tina67@example.com",
            "hand": "",
            "id": 1,
            "name": "angela schroeder94",
            "sex": "male",
            "table_stakes": null
            }

# Group Tables

## Tables [/tables]

### Retrieve List of Tables [GET]

    + Response 200 (application/json)
        + Attributes [(object),(object)]
            + id: 1 (integer, auto-incremented, unique)
            + game_type: (string, required, not null)
            + min_stake: (integer, required, not null)
            + max_stake: (integer, required, not null)
            + hole_cards: (string)
            + pot_amount: (integer)
            + is_girls_only: (bool)
        + Body
            [{
            "game_type": "catherine ortiz",
            "hole_cards": "",
            "id": 1,
            "is_girls_only": false,
            "max_stake": 15000,
            "min_stake": 1500,
            "pot_amount": 1176
            },
            {
            "game_type": "shannon vargas",
            "hole_cards": "",
            "id": 2,
            "is_girls_only": false,
            "max_stake": 15000,
            "min_stake": 1500,
            "pot_amount": 642
            }]

## Tables [/tables/{id}]

### Retrieve a single table [GET]

returns a single json object

    + Parameters
        + id: 1 (int) - An unique identifier of the message.
    + Response 200 (application/json)
        + Body:
            {
            "game_type": "robert cox dvm",
            "hole_cards": "",
            "id": 14,
            "is_girls_only": false,
            "max_stake": 15000,
            "min_stake": 1500,
            "pot_amount": 278
            }
