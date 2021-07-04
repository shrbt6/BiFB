import re, photo_file, app_sqlite
from app_sqlite import exec, select

# usersテーブル
def add_user(user_id, user_name, email):
    checked_id = select('SELECT * FROM users WHERE user_id=?', user_id)
    if len(checked_id) == 0:
        exec('INSERT INTO users (user_id, user_name, email) VALUES (?,?,?)', user_id, user_name, email)

def get_user_name(user_id):
    a = select('SELECT * FROM users WHERE user_id=?', user_id)
    if len(a) == 0:
        return None
    return a[0]['user_name']

def get_user_point(user_id):
    point = select('SELECT point FROM users WHERE user_id=?', user_id)
    return point[0]['point']

def sum_user_point(user_id):
    point = select('SELECT point FROM users WHERE user_id=?', user_id)
    if len(point):
        new_point_val = point[0]['point'] + 1
        exec('UPDATE users SET point=? WHERE user_id=?', new_point_val, user_id)
        return new_point_val
    return None

def sub_user_point(user_id):
    point = select('SELECT point FROM users WHERE user_id=?', user_id)
    if len(point):
        new_point_val = max(point[0]['point']-1, 0)
        exec('UPDATE users SET point=? WHERE user_id=?', new_point_val, user_id)
        return new_point_val
    return None

# appsテーブル
def add_app(user_id, title, description, url):
    search_app = select('SELECT * FROM apps WHERE user_id=? AND title=?', user_id, title)
    if len(search_app)==0:
        app_id = exec('INSERT INTO apps (user_id, title, description, url) VALUES (?,?,?,?)', user_id, title, description, url)
        return app_id
    else:
        return None

def get_apps():
    a = select('SELECT * FROM apps')
    for i in a:
        i['user_name'] = get_user_name(i['user_id'])
    return a

def get_apps_within_deadline():
    a = select('SELECT * FROM apps WHERE limit_at >= date("now", "localtime")')
    for i in a:
        i['user_name'] = get_user_name(i['user_id'])
    return a

def get_app(app_id):
    a = select('SELECT * FROM apps WHERE app_id=?', app_id)
    if len(a) == 0:
        return None
    a[0]['user_name'] = get_user_name(a[0]['user_id'])
    return a[0]

def add_feedback(user_id, app_id, title, description):
    feedback_id = exec('INSERT INTO feedback (user_id, app_id, title, description) VALUES (?,?,?,?)', user_id, app_id, title, description)
    return feedback_id

# def remove_feedback(feedback_id):

def get_feedback_of_app(app_id):
    a = select('SELECT * FROM feedback WHERE app_id=?', app_id)
    if len(a) == 0:
        return None
    return a

# def get_user_point():