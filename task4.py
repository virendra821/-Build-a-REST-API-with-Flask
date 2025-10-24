from flask import Flask, request, jsonify

app = Flask(__name__)
user_records = {}

@app.route("/")
def home():
    return "<h2>✅ Flask API is running! Visit /users to view or manage users.</h2>"

@app.route("/users", methods=["GET"])
def see_all_users():
    return jsonify(user_records), 200

@app.route("/users", methods=["POST"])
def create_new_user():
    details = request.get_json()
    new_id = str(len(user_records) + 1)
    user_records[new_id] = {
        "name": details.get("name"),
        "email": details.get("email")
    }
    return jsonify({"message": "User added successfully!", "user": user_records[new_id]}), 201

@app.route("/users/<user_id>", methods=["PUT"])
def change_user_info(user_id):
    if user_id not in user_records:
        return jsonify({"error": "User not found!"}), 404
    
    updates = request.get_json()
    
    user_records[user_id].update({
        "name": updates.get("name", user_records[user_id]["name"]),
        "email": updates.get("email", user_records[user_id]["email"])
    })
    
    return jsonify({"message": "User updated successfully!", "user": user_records[user_id]}), 200

@app.route("/users/<user_id>", methods=["DELETE"])
def remove_user(user_id):
    if user_id not in user_records:
        return jsonify({"error": "User not found!"}), 404
        
    removed_user = user_records.pop(user_id)
    return jsonify({"message": "User deleted successfully!", "user": removed_user}), 200

if __name__ == "__main__":
    app.run(debug=True)
