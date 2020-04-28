from flask import Flask, jsonify, request
from flask_pymongo import PyMongo
from bson.json_util import dumps, ObjectId
from werkzeug.security import generate_password_hash, check_password_hash


app = Flask(__name__)
app.secret_key = "secretkey"
app.config['MONGO_URI'] = "mongodb://nusta_coder:shadow7431@cluster0-shard-00-00-kwsyr.mongodb.net:27017,cluster0-shard-00-01-kwsyr.mongodb.net:27017,cluster0-shard-00-02-kwsyr.mongodb.net:27017/shadow?ssl=true&replicaSet=Cluster0-shard-0&authSource=admin&retryWrites=true&w=majority"

mongo = PyMongo(app)


@app.route('/', methods=['GET'])
def index():
    rep = jsonify("hello world")
    return rep


@app.errorhandler(404)
def notFound(error=None):
    message = {
        'status': 404,
        'message': 'not found' + request.url
    }

    resp = jsonify(message)
    resp.status_code = 404

    return resp


@app.route('/users', methods=['GET'])
def getUsers():
    users = mongo.db.login.find()
    resp = dumps(users)
    return resp


@app.route('/user/<id>', methods=['GET'])
def getUser(id):
    user = mongo.db.login.find({"_id": ObjectId(id)})
    resp = dumps(user)
    return resp


@app.route('/add', methods=['POST'])
def addUser():
    _json = request.json
    _name = _json['name']
    _password = _json['password']

    if _name and _password and request.method == 'POST':
        _hasedpwd = generate_password_hash(_password)
        id = mongo.db.login.insert({"name": _name, "password": _hasedpwd})
        resp = jsonify("user entered succefully")
        resp.status_code = 200
        return resp
    return notFound()


@app.route('/delete/<id>', methods=['DELETE'])
def deleteUser(id):
    user = {"_id": ObjectId(id)}
    id = mongo.db.login.delete_one(user)
    resp = jsonify("usre deleted succesfully")
    resp.status_code = 200
    return resp


if __name__ == "__main__":
    app.run(debug=True)
