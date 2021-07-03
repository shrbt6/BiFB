from flask import Flask, render_template, request
from flask.wrappers import Request
import app_db

app = Flask(__name__)

@app.route('/')
def hello():
    return render_template('index.html', apps=app_db.get_apps())

@app.route('/login')
def login():
    return render_template('login_form.html')

@app.route('/user/add', methods=['POST'])
def add_user():
    user_data = request.json
    app_db.add_user(user_data['user_id'], user_data['user_name'], user_data['email'])
    return user_data

@app.route('/post')
def post():
    return render_template('application_post.html')

@app.route('/post/try', methods=['POST'])
def register_user():
    if request.method == 'POST':
        app_title = request.form['app_title']
        app_description = request.form['app_description']
        app_url = request.form['app_url']
        user_id = request.form['user_id']
        app_db.add_user(user_id)
        app_db.add_app(user_id, app_title, app_description, app_url)
    return render_template('index.html', apps=app_db.get_apps())

if __name__ == '__main__':
    app.run(debug=True)