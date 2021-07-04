from flask import Flask, render_template, request
from flask.wrappers import Request
import app_db

app = Flask(__name__)

@app.route('/')
def hello():
    return render_template('index.html', apps=app_db.get_apps_within_deadline())

@app.route('/login')
def login():
    return render_template('login_form.html')

@app.route('/add/user', methods=['POST'])
def add_user():
    user_data = request.json
    app_db.add_user(user_data['user_id'], user_data['user_name'], user_data['email'])
    return user_data

@app.route('/post')
def post():
    # 先にポイントを見てポイントが0なら投稿できないようにする
    return render_template('application_post.html')

@app.route('/post/try', methods=['POST'])
def post_try():
    if request.method == 'POST':
        app_title = request.form['app_title']
        app_description = request.form['app_description']
        app_url = request.form['app_url']
        user_id = request.form['user_id']
        app_db.add_app(user_id, app_title, app_description, app_url)
    return render_template('index.html', apps=app_db.get_apps_within_deadline())

@app.route('/app/<app_id>')
def app_details(app_id):
    return render_template('app_details.html',
                        app=app_db.get_app(app_id),
                        feedback=app_db.get_feedback_of_app(app_id))

@app.route('/feedback/<app_id>')
def add_feedback(app_id):
    return render_template('feedback.html', app_id=app_id)

if __name__ == '__main__':
    app.run(debug=True)