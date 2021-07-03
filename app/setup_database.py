from app_sqlite import exec

exec('''
CREATE TABLE users (
    user_id     TEXT PRIMARY KEY,
    point       INTEGER default 1;
)
''')

exec('''
CREATE TABLE apps (
    app_id      INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id     TEXT PRIMARY KEY,
    title       TEXT,
    description TEXT,
    url         TEXT,
    filename    TEXT,
    created_at  TIMESTAMP DEFAULT (DATETIME('now', 'localtime'))
    limit       TIMESTAMP DEFAULT (DATETIME('now', 'localtime')) + INTEGER '30'
)
''')

exec('''
CREATE TABLE feedback (
    feedback_id     INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id         TEXT PRIMARY KEY,
    title           TEXT,
    description     TEXT,
    created_at      TIMESTAMP DEFAULT (DATETIME('now', 'localtime'))
)
''')