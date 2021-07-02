from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

@app.route("/hello")
def hello1():
    return "こんにちは"

if __name__ == "__main__":
    app.run(debug=True)