from flask import Flask, request, jsonify, send_from_directory

app = Flask(__name__)

todos = []
todo_id_counter = 1

@app.route("/")
def serve_frontend():
    return send_from_directory("", "index.html")

@app.route("/todos", methods=["GET"])
def get_todos():
    return jsonify(todos)

@app.route("/todos", methods=["POST"])
def add_todo():
    global todo_id_counter
    title = request.json.get("title")
    if not title:
        return jsonify({"error": "Title is required"}), 400
    new_todo = {"id": todo_id_counter, "title": title}
    todos.append(new_todo)
    todo_id_counter += 1
    return jsonify(new_todo), 201

@app.route("/todos/<int:id>", methods=["DELETE"])
def delete_todo(id):
    todo = next((todo for todo in todos if todo["id"] == id), None)
    if todo is None:
        return jsonify({"error": "To-Do not found"}), 404
    todos.remove(todo)
    return jsonify({"message": "To-Do deleted"}), 200

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
