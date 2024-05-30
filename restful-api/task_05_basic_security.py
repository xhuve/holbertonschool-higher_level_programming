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

@app.route("/basic-protected")
@auth.login_required
def basicRoute():
    print(auth.current_user())
    return "Basic Auth: Access Granted"

@auth.verify_password
def verify_password(username, password):
    if username in users and check_password_hash(users[username].get("password"), password):
        access_token = create_access_token(identity=username)
        return jsonify(access_token)

if __name__ == "__main__": 
    app.run()
