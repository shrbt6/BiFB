from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello World!'

@app.route('/test')
def hello1():
    return render_template('test.html')

@app.route('/login')
def login():
    return render_template('login_form.html')

@app.route('/success')
def success():
    return '認証成功'

if __name__ == '__main__':
    app.run(debug=True)