from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello World!'

@app.route('/test')
def hello1():
    return render_template('test.html')

if __name__ == '__main__':
    app.run(debug=True)