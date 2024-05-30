#!/usr/bin/python3
from flask import Flask, jsonify, request
from flask_httpauth import HTTPBasicAuth
from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import JWTManager, create_access_token

app = Flask(__name__)
auth = HTTPBasicAuth()
app.config["JWT_SECRET_KEY"] = "secret-key"
jwt = JWTManager(app)


users = {
    "billy": {"username": "billy", "password": generate_password_hash("billijean"), "role": "admin"}
}

@auth.verify_password
def verify_password(username, password):
    user = users.get(username)
    if user and check_password_hash(users[username].get("password"), password):
        return username

@app.route("/basic-protected")
@auth.login_required
def basicRoute():
    return {"msg": "Basic Auth: Access Granted"}

if __name__ == "__main__": 
    app.run()
