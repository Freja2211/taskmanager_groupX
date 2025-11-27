import sqlite3
from model.task import Task

def get_connection():
    return sqlite3.connect("tasks.db")

def init_storage():
    with get_connection() as conn:
        conn.execute("""
            CREATE TABLE IF NOT EXISTS tasks (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT,
                description TEXT,
                status TEXT
            )
        """)

def save_task(title, description):
    with get_connection() as conn:
        cur = conn.execute(
            "INSERT INTO tasks (title, description, status) VALUES (?, ?, ?)",
            (title, description, "todo")
        )
        newid = cur.lastrowid
        inserted = conn.execute("SELECT id, title, description, status FROM tasks WHERE id = ?", (newid,)).fetchone()
    return Task(inserted[1], inserted[2], inserted[3], inserted[0])

def get_tasks():
    with get_connection() as conn:
        rows = conn.execute("SELECT id, title, description, status FROM tasks").fetchall()
    return [Task(row[1], row[2], row[3], row[0]) for row in rows]

def update_task(task, status):
    with get_connection() as conn:
        conn.execute("UPDATE tasks SET status = ? WHERE id = ?", (status, task.id))
        updated = conn.execute("SELECT id, title, description, status FROM tasks WHERE id = ?", (task.id,)).fetchone()
    return Task(updated[1], updated[2], updated[3], updated[0])

def delete_task(task):
    with get_connection() as conn:
        conn.execute("DELETE FROM tasks WHERE id = ?", (task.id,))
        deleted = conn.execute("SELECT id, title, description, status FROM tasks WHERE id = ?", (task.id,)).fetchone()
    return Task(deleted[1], deleted[2], deleted[3], deleted[0])
