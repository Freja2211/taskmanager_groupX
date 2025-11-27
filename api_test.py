import requests

# 1. POST – opret ny opgave
response = requests.post(
    "http://127.0.0.1:5000/tasks",
    json={"title": "Testopgave", "description": "Lav et API-kald"}
)
print("POST status:", response.status_code)
print("POST result:", response.json())

# 2. PUT – marker som done
task_id = response.json().get("id", 1)  # fallback hvis id mangler
response = requests.put(f"http://127.0.0.1:5000/tasks/{task_id}/done")
print("PUT status:", response.status_code)
print("PUT result:", response.json())

# 3. GET – hent alle
response = requests.get("http://127.0.0.1:5000/tasks")
print("GET result:", response.json())