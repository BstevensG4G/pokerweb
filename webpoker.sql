-- kill other connections
SELECT pg_terminate_backend(pg_stat_activity.pid)
FROM pg_stat_activity
WHERE pg_stat_activity.datname = 'webpoker' AND pid <> pg_backend_pid();
-- (re)create the database
DROP DATABASE IF EXISTS webpoker;
CREATE DATABASE webpoker;
-- connect via psql
\c webpoker

-- database configuration
SET statement_timeout = 0;
SET lock_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SET check_function_bodies = false;
SET client_min_messages = warning;
SET default_tablespace = '';
SET default_with_oids = false;

---
--- CREATE card_tables
---

CREATE TABLE card_tables (
    id SERIAL,
    pot_amount INT,
    min_stake INT NOT NULL DEFAULT 5000,
    max_stake INT NOT NULL DEFAULT 50000,
    hole_cards TEXT DEFAULT '',
    game_type TEXT NOT NULL,
    is_girls_only BOOLEAN NOT NULL DEFAULT 'false',
    PRIMARY KEY (id)
);

CREATE TABLE players (
    id SERIAL,
    name TEXT NOT NULL,
    email TEXT NOT NULL UNIQUE,
    password TEXT NOT NULL,
    sex TEXT NOT NULL, -- needed for girl only gameplay --
    hand TEXT DEFAULT '',
    bankroll INT NOT NULL DEFAULT 25000,
    table_stakes INT DEFAULT 0,
    current_bet INT DEFAULT 0,
    PRIMARY KEY (id)
);

CREATE TABLE deck_of_cards (
    id SERIAL,
    card_value INT NOT NULL,
    card_suit CHAR(12) NOT NULL,
    deck_num INT NOT NULL,
    UNIQUE (card_value, card_suit, deck_num),
    PRIMARY KEY (id)
);

CREATE TABLE dealers (
    id SERIAL,
    name TEXT DEFAULT 'Gus',
    deck_id INT NOT NULL,
    PRIMARY KEY (id)
);

-- Table created for many to many relationship
CREATE TABLE tables_players (
    table_id INT,
    player_id INT,
    PRIMARY KEY (table_id, player_id)
);

---
--- FOREIGN KEY CONSTRAINTS
---

ALTER TABLE dealers
ADD CONSTRAINT fk_dealers_decks
FOREIGN KEY (deck_id)
REFERENCES deck_of_cards (id);

ALTER TABLE tables_players
ADD CONSTRAINT fk_tables_players_players 
FOREIGN KEY (player_id)
REFERENCES players (id);

ALTER TABLE tables_players
ADD CONSTRAINT fk_tables_players_tables 
FOREIGN KEY (table_id) 
REFERENCES tables (id);

---
--- Data Inserts
---

INSERT INTO deck_of_cards (card_value, card_suit, deck_num)
VALUES (generate_series(2,14), 'hearts', 1);
INSERT INTO deck_of_cards (card_value, card_suit, deck_num)
VALUES (generate_series(2,14), 'spades', 1);
INSERT INTO deck_of_cards (card_value, card_suit, deck_num)
VALUES (generate_series(2,14), 'clubs', 1);
INSERT INTO deck_of_cards (card_value, card_suit, deck_num)
VALUES (generate_series(2,14), 'diamonds', 1);

INSERT INTO deck_of_cards (card_value, card_suit, deck_num)
VALUES (generate_series(2,14), 'hearts', 2);
INSERT INTO deck_of_cards (card_value, card_suit, deck_num)
VALUES (generate_series(2,14), 'diamonds', 2);
INSERT INTO deck_of_cards (card_value, card_suit, deck_num)
VALUES (15, 'red joker', 2);
INSERT INTO deck_of_cards (card_value, card_suit, deck_num)
VALUES (generate_series(2,14), 'spades', 2);
INSERT INTO deck_of_cards (card_value, card_suit, deck_num)
VALUES (generate_series(2,14), 'clubs', 2);
INSERT INTO deck_of_cards (card_value, card_suit, deck_num)
VALUES (16, 'black joker', 2);

INSERT INTO dealers (deck_id)
VALUES (1);
INSERT INTO dealers (name, deck_id)
VALUES ('Bill', 2);

INSERT INTO players (name, email, password, sex)
VALUES ('Brett', 'brett@email.com', 'P@ssw0rd', 'male');
INSERT INTO players (name, email, password, sex)
VALUES ('Sam', 'sam@email.com', 'P@ssw0rd', 'male');
INSERT INTO players (name, email, password, sex)
VALUES ('Tony', 'tony@email.com', 'P@ssw0rd', 'male');
INSERT INTO players (name, email, password, sex)
VALUES ('Jeff', 'jeff@email.com', 'P@ssw0rd', 'male');
INSERT INTO players (name, email, password, sex)
VALUES ('Mike', 'mike@email.com', 'P@ssw0rd', 'male');

INSERT INTO players (name, email, password, sex)
VALUES ('Diane', 'diane@email.com', 'P@ssw0rd', 'female');
INSERT INTO players (name, email, password, sex)
VALUES ('Laura', 'laura@email.com', 'P@ssw0rd', 'female');
INSERT INTO players (name, email, password, sex)
VALUES ('Beth', 'beth@email.com', 'P@ssw0rd', 'female');
INSERT INTO players (name, email, password, sex)
VALUES ('suzy', 'suzy@email.com', 'P@ssw0rd', 'female');
INSERT INTO players (name, email, password, sex)
VALUES ('Mary', 'mary@email.com', 'P@ssw0rd', 'female');

INSERT INTO tables (min_stake, max_stake, game_type)
VALUES (25000, 500000, 'Holdem');
INSERT INTO tables (game_type)
VALUES ('Holdem');
INSERT INTO tables (min_stake, max_stake, game_type)
VALUES (1000, 5000, 'Girls only Holdem');
INSERT INTO tables (min_stake, max_stake, game_type)
VALUES (10000, 30000, 'Omaha');
INSERT INTO tables (min_stake, max_stake, game_type)
VALUES (5000, 25000, 'Omaha hi/lo');

INSERT INTO tables_players (table_id, player_id)
VALUES (3,6);
INSERT INTO tables_players (table_id, player_id)
VALUES (3,7);
INSERT INTO tables_players (table_id, player_id)
VALUES (1,1);
INSERT INTO tables_players (table_id, player_id)
VALUES (1,4);
INSERT INTO tables_players (table_id, player_id)
VALUES (1,5);
INSERT INTO tables_players (table_id, player_id)
VALUES (5, 2);
INSERT INTO tables_players (table_id, player_id)
VALUES (5, 3);
INSERT INTO tables_players (table_id, player_id)
VALUES (4, 8);