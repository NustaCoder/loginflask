from flask import Flask, jsonify, request
from bson.json_util import dumps

app = Flask(__name__)
app.secret_key = "secretkey"


@app.route('/')
def myIndex():
    rep = jsonify("index page")
    return rep


@app.route('/login')
def myLogIn():
    _json = request.json
    name = _json['name']
    surname = _json['surname']

    return name+" "+surname


@app.route('/add')
def showUsers():
    _json = request.json
    a = _json['a']
    b = _json['b']
    c = a+b
    return str(c)


@app.route('/mul')
def deleteUser():
    _json = request.json
    a = _json['a']
    b = _json['b']
    c = a*b
    return str(c)


@app.route('/sub')
def updateUser():
    _json = request.json
    a = _json['a']
    b = _json['b']
    c = a-b
    return str(c)


if __name__ == "__main__":
    app.run(debug=True)
