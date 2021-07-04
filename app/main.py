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
    return render_template('application_post.html')

@app.route('/post/try', methods=['POST'])
def post_try():
    if request.method == 'POST':
        app_title = request.form['app_title']
        app_description = request.form['app_description']
        app_url = request.form['app_url']
        user_id = request.form['user_id']
        app_id = app_db.add_app(user_id, app_title, app_description, app_url)
        if app_id:
            point = app_db.sub_user_point(user_id)
    return render_template('index.html', apps=app_db.get_apps_within_deadline())

@app.route('/app/<app_id>')
def app_details(app_id):
    return render_template('app_details.html',
                        app=app_db.get_app(app_id),
                        feedback=app_db.get_feedback_of_app(app_id))

@app.route('/feedback/<app_id>')
def feedback(app_id):
    return render_template('feedback.html', app_id=app_id)

@app.route('/add/feedback', methods=['POST'])
def add_feedback():
    if request.method == 'POST':
        feedback_user_id = request.form['feedback_user_id']
        feedback_app_id = request.form['feedback_app_id']
        feedback_title = request.form['feedback_title']
        feedback_description = request.form['feedback_description']
        feedback_id = app_db.add_feedback(feedback_user_id, feedback_app_id, feedback_title, feedback_description)
        if feedback_id:
            point = app_db.sum_user_point(feedback_user_id)
    return render_template('app_details.html',
                        app=app_db.get_app(feedback_app_id),
                        feedback=app_db.get_feedback_of_app(feedback_app_id))

if __name__ == '__main__':
    app.run(debug=True)