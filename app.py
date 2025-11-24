from flask import Flask, request, jsonify
from db import get, post, put, delete

app = Flask(__name__)

@app.route("/users", methods=["GET"])
def get_users():
    return jsonify(get())

@app.route("/users", methods=["POST"])
def create_user():
    data = request.json
    return jsonify(post(data))

@app.route("/users/<int:user_id>", methods=["PUT"])
def update_user(user_id):
    data = request.json
    return jsonify(put(user_id, data))

@app.route("/users/<int:user_id>", methods=["DELETE"])
def remove_user(user_id):
    return jsonify(delete(user_id))

if __name__ == "__main__":
    app.run(debug=True)
