#!/usr/bin/python3
from flask import Flask, jsonify, request
import json

app = Flask(__name__)

users = {"jane": {"name": "Jane", "age": 28, "city": "Los Angeles"}}

@app.route('/')
def home():
    return "Welcome to the Flask API!"

@app.route('/data')
def JsonData():
    all_keys = [key for key in users.keys()]
    return jsonify(all_keys)

@app.route('/status')
def ServerStatus():
    return "OK"

@app.route('/users/<username>')
def ReturnUser(username):
    user = users.get(username)
    if user:
        return jsonify(user)
    else:
        return jsonify({"error": "User not found"}), 404
        

@app.post("/add_user")
def AddUsers():
    data = request.get_json()
    users[data["username"]] = {key: data[key] for key in ['name', 'age', 'city']}
    return { "message": "User added", "user": data}

if __name__ == "__main__":
    app.run()