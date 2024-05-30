#!/usr/bin/python3
from flask import Flask, jsonify, request
from flask_httpauth import HTTPBasicAuth
from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity

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
    return "Basic Auth: Access Granted"

@app.post("/login")
def loginRoute():
    data = request.json
    username = data.get("username")
    password = data.get("password")
    if users.get(username) and check_password_hash(users[username].get("password"), password):
        return {"access_token": create_access_token(identity=username)}

@app.get("/jwt-protected")
@jwt_required()
def jwtRoute():
    curr_user = get_jwt_identity()
    return jsonify({"logged_in": curr_user})


@auth.error_handler
def unauthorized():
    return jsonify({"message": "Unauthorized"}), 401

if __name__ == "__main__": 
    app.run()
