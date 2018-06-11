from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Welcome Home"

@app.route("/cherry")
def cherry():
    return "Welcome to my home"
