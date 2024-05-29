from flask import Flask, jsonify, request
import json

app = Flask(__name__)

users = {"jane": {"name": "Jane", "age": 28, "city": "Los Angeles"}}


@app.route('/')
def home():
    return "Welcome to Flask API!"

@app.route('/data')
def JsonData():
    all_keys = [key for key in users.keys()]
    return jsonify(all_keys)

@app.route('/status')
def ServerStatus():
    return "Ok"

@app.route('/users/<username>')
def ReturnUser(username):
    jData = json.loads(jsonify(users).data)
    return jData[username]

@app.post("/add_user")
def AddUsers():
    data = request.get_json()
    users[data["username"]] = {key: data[key] for key in ['name', 'age', 'city']}
    return { "message": "User added", "user": data}

if __name__ == "__main__":
    app.run()