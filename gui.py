import tkinter as tk
import requests

API_URL = "http://127.0.0.1:5000/tasks"

def load_tasks():
    task_list.delete(0, tk.END)
    try:
        for t in requests.get(API_URL).json():
            task_list.insert(tk.END, f"{t['id']}: {t['title']}")
    except Exception as e:
        task_list.insert(tk.END, f"Fejl: {e}")

def add_task():
    title = title_entry.get().strip()
    if title:
        requests.post(API_URL, json={"title": title, "description": ""})
        title_entry.delete(0, tk.END)
        load_tasks()

root = tk.Tk()
root.title("Tasks")

tk.Label(root, text="Opgaver").pack()
task_list = tk.Listbox(root, width=40, height=10)
task_list.pack()

tk.Button(root, text="Opdater", command=load_tasks).pack(pady=2)

frame = tk.Frame(root)
frame.pack(pady=5)
title_entry = tk.Entry(frame, width=25)
title_entry.pack(side=tk.LEFT)
tk.Button(frame, text="Tilføj", command=add_task).pack(side=tk.LEFT, padx=5)

load_tasks()
root.mainloop()