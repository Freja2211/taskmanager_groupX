# api.py
from flask import Flask, jsonify, request
from task_manager import get_all_tasks, create_task

app = Flask(__name__)

@app.route("/tasks", methods=["GET"])
def list_tasks():
    tasks = get_all_tasks()
    return jsonify([t.__dict__ for t in tasks])

@app.route("/tasks", methods=["POST"])
def add_task():
    data = request.get_json()
    new = create_task(data["title"], data["description"])
    return jsonify(new.__dict__), 201

if __name__ == "__main__":
    app.run(debug=True)

@app.route("/tasks/<int:id>/done",methods=["put]"])
def mark_done(id):
 from task_manager import update_task
 task = update_task(id,"done")
 return jsonify(task.__dict__)