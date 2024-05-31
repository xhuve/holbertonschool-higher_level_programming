#!/usr/bin/python3
from flask import Flask, jsonify, request
from flask_httpauth import HTTPBasicAuth
from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity

app = Flask(__name__)

app.config["SECRET_KEY"] = 'testkey'
app.config["JWT_SECRET_KEY"] = "secret-key"

auth = HTTPBasicAuth()
jwt = JWTManager(app)


users = {
    "user1": {"username": "user1", "password": generate_password_hash("user1"), "role": "user"},
    "admin1": {"username": "admin1", "password": generate_password_hash("admin1"), "role": "admin"}
}

@auth.verify_password
def verify_password(username, password):
    user = users.get(username)
    if user and check_password_hash(user.get("password"), password):
        return user

@app.route("/basic-protected")
@auth.login_required
def basicRoute():
    return "Basic Auth: Access Granted"

@app.post("/login")
def loginRoute():
    data = request.get_json()
    username = data.get("username")
    password = data.get("password")
    user = users.get(username)
    if user and check_password_hash(user.get("password"), password):
        access_token = create_access_token(identity={"username": username, "role": user.get("role")})
        return jsonify({"access_token": access_token})
    else:
        return jsonify({ "error": "Invalid Credentials" }), 401

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
        return jsonify("403 Forbidden"), 403

@jwt.unauthorized_loader
def handle_unauthorized_error(err):
    return jsonify({"error": "Missing or invalid token"}), 401

@jwt.invalid_token_loader
def handle_invalid_token_error(err):
    return jsonify({"error": "Invalid token"}), 401

@jwt.expired_token_loader
def handle_expired_token_error(err):
    return jsonify({"error": "Token has expired"}), 401

@jwt.revoked_token_loader
def handle_revoked_token_error(err):
    return jsonify({"error": "Token has been revoked"}), 401

@jwt.needs_fresh_token_loader
def handle_needs_fresh_token_error(err):
    return jsonify({"error": "Fresh token required"}), 401

if __name__ == "__main__": 
    app.run()
