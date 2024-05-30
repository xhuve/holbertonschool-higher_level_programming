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
    "user1": {"username": "user1", "password": generate_password_hash("user1"), "role": "user"},
    "admin1": {"username": "admin1", "password": generate_password_hash("admin1"), "role": "admin"}
}

@auth.verify_password
def verify_password(username, password):
    user = users.get(username)
    if user and check_password_hash(user.get("password"), password):
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
    return "JWT Auth: Access Granted"

@app.route("/admin-only")
@jwt_required()
def adminRoute():
    user = get_jwt_identity()
    if user and users[user].get("role") == "admin":
        return "Admin Access: Granted"
    else:
        return "403 Forbidden", 403

@auth.error_handler
def unauthorized():
    return jsonify({"message": "Unauthorized"}), 401

if __name__ == "__main__": 
    app.run()
