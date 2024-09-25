CREATE TABLE IF NOT EXISTS users
(
    id       INTEGER PRIMARY KEY AUTOINCREMENT,
    email    TEXT NOT NULL UNIQUE,
    password TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS players
(
    user_id  INTEGER PRIMARY KEY,
    nickname TEXT    NOT NULL UNIQUE,
    balance  INTEGER NOT NULL,
    FOREIGN KEY (user_id) REFERENCES users (id)
);

CREATE TABLE IF NOT EXISTS items
(
    id       INTEGER PRIMARY KEY AUTOINCREMENT,
    name     TEXT    NOT NULL UNIQUE,
    price    INTEGER NOT NULL,
    owner_id INTEGER,
    FOREIGN KEY (owner_id) REFERENCES players (user_id)
);
