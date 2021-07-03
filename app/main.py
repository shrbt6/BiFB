from flask import Flask, render_template, request
from flask.wrappers import Request
from werkzeug.utils import redirect
app = Flask(__name__)

@app.route('/')
def hello():
    return render_template('index.html')

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
    return render_template('index.html')

@app.route('/login')
def login():
    return render_template('login_form.html')

if __name__ == '__main__':
    app.run(debug=True)