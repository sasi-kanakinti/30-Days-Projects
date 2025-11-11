from flask import Flask, jsonify, request

app = Flask(__name__)


users = [
    {"id": 1, "name": "Alice", "role": "Developer"},
    {"id": 2, "name": "Bob", "role": "Tester"}
]


@app.route('/users', methods=['GET'])
def get_users():
    return jsonify(users)


@app.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    user = next((u for u in users if u["id"] == user_id), None)
    return jsonify(user if user else {"error": "User not found"}), 200 if user else 404


@app.route('/users', methods=['POST'])
def add_user():
    new_user = request.get_json()
    users.append(new_user)
    return jsonify({"message": "User added", "data": new_user}), 201


@app.route('/users/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    updated_data = request.get_json()
    for u in users:
        if u["id"] == user_id:
            u.update(updated_data)
            return jsonify({"message": "User updated", "data": u})
    return jsonify({"error": "User not found"}), 404


@app.route('/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    global users
    users = [u for u in users if u["id"] != user_id]
    return jsonify({"message": f"User with id {user_id} deleted"})

if __name__ == '__main__':
    app.run(debug=True)
