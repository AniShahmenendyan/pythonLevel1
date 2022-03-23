from flask import Flask
from flask import request
from flask import render_template

app = Flask(__name__)


@app.route("/")
def hello_world():
    return render_template('home.html')


@app.route("/users")
def users():
    response = "<p>Users</p>"
    return response


@app.route("/users/<id>")
def user(id):
    response = f"<p>User information {id}</p>"
    return response
