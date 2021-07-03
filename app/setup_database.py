from app_sqlite import exec

exec('''
CREATE TABLE users (
    user_id     TEXT PRIMARY KEY,
    user_name   TEXT,
    email       TEXT,
    point       INTEGER default 1
)
''')

exec('''
CREATE TABLE apps (
    app_id      INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id     TEXT,
    title       TEXT,
    description TEXT,
    url         TEXT,
    filename    TEXT,
    created_at  TIMESTAMP DEFAULT (DATE('now', 'localtime')),
    limit_at    TIMESTAMP DEFAULT (DATE('now', 'localtime', '+30 days'))
)
''')

exec('''
CREATE TABLE feedback (
    feedback_id     INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id         TEXT,
    app_id          INTEGER,
    title           TEXT,
    description     TEXT,
    created_at      TIMESTAMP DEFAULT (DATETIME('now', 'localtime'))
)
''')