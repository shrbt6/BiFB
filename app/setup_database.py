from app_sqlite import exec

exec('''
CREATE TABLE apps (
    app_id      INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id     INTEGER,
    title       TEXT,
    description TEXT,
    url         TEXT,
    filename    TEXT,
    created_at  TIMESTAMP DEFAULT (DATETIME('now', 'localtime'))
)
''')

exec('''
CREATE TABLE feedback (
    feedback_id     INTEGER PRIMARY KEY AUTOINCREMENT,
    title           TEXT,
    description     TEXT,
    created_at      TIMESTAMP DEFAULT (DATETIME('now', 'localtime'))
)
''')