from flask import Flask, jsonify, request

app = Flask(__name__)

# Tymczasowe dane - docelowo powinna byc baza danych
tasks = [
    {"id": 1, "title": "Zrobic herbate", "done": False},
    {"id": 2, "title": "Odpalic laptopa", "done": False},
    {"id": 3, "title": "Uruchomic aplikacje", "done": False},
]

@app.route("/")
def index():
    return jsonify({"message": "Task Manager API"})

@app.route("/health")
def health():
    return jsonify({"status": "ok"})

@app.route("/tasks", methods=["GET"])
def get_tasks():
    return jsonify(tasks)

@app.route("/tasks", methods=["POST"])
def add_task():
    data = request.get_json()

    if not data or "title" not in data:
        return jsonify({"error": "Brakuje tytulu zadania"}), 400

    task = {
        "id": len(tasks) + 1,
        "title": data["title"],
        "done": False
    }
    tasks.append(task)
    return jsonify(task), 201

@app.route("/tasks/<int:task_id>/done", methods=["PUT"])
def complete_task(task_id):
    task = None
    for t in tasks:
        if t["id"] == task_id:
            task = t
            break
    if task is None:
        return jsonify({"error": "Nie ma takiego zadania"}), 404
    task["done"] = True
    return jsonify(task)
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
