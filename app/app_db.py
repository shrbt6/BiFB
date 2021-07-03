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

def sum_user_point(user_id):
    point = select('SELECT point FROM users WHERE user_id=?', user_id)
    if len(point):
        new_point_val = point[0] + 1
        exec('UPDATE users SET point=? WHERE user_id=?', new_point_val, user_id)
        return new_point_val
    return None

def sub_user_point(user_id):
    point = select('SELECT point FROM users WHERE user_id=?', user_id)
    if len(point):
        new_point_val = max(point[0]-1, 0)
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
    return a[0]

def album_new(user_id, args):
    name = args.get('name', '')
    if name == '':
        return 0
    album_id = exec('INSERT INTO albums (name, user_id) VALUES (?,?)', name, user_id)
    return album_id

def get_albums(user_id):
    return select('SELECT * FROM albums WHERE user_id=?', user_id)

def get_album(album_id):
    a = select('SELECT * FROM albums WHERE album_id=?', album_id)
    if len(a) == 0:
        return None
    return a[0]

def get_album_name(album_id):
    a = get_album(album_id)
    if a == None:
        return '未分類'
    return a['name']

def save_file(user_id, upfile, album_id):
    if not re.search(r'\.(jpg|jpeg)$', upfile.filename):
        print('JPEGではない：', upfile.filename)
        return 0
    
    if album_id == 0:
        a = select('SELECT * FROM albums WHERE user_id=? AND name=?', user_id, '未分類')
        if len(a) == 0:
            album_id = exec('INSERT INTO albums (user_id, name) VALUES (?,?)', user_id, '未分類')
        else:
            album_id = a[0]['album_id']

    file_id = exec('''
        INSERT INTO files (user_id, filename, album_id) VALUES (?,?,?)
    ''', user_id, upfile.filename, album_id)
    upfile.save(photo_file.get_path(file_id))
    return file_id

def get_file(file_id, ptype):
    a = select('SELECT * FROM files WHERE file_id=?', file_id)
    if len(a) == 0:
        return None
    p = a[0]
    p['path'] = photo_file.get_path(file_id)
    if ptype == 'thumb':
        p['path'] = photo_file.make_thubnail(file_id, 300)
    return p

def get_files():
    a = select('SELECT * FROM files ORDER BY file_id DESC LIMIT 50')
    for i in a:
        i['name'] = get_album_name(i['album_id'])
    return a

def get_album_files(album_id):
    return select('SELECT * FROM files WHERE album_id=? ORDER BY file_id DESC', album_id)

def get_user_files(user_id):
    a = select('SELECT * FROM files WHERE user_id=? ORDER BY file_id DESC LIMIT 50', user_id)
    for i in a:
        i['name'] = get_album_name(i['album_id'])
    return a