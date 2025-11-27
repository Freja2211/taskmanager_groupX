class Task:
    def __init__(self, title, description, status="todo", id=None):
        self.id = id
        self.title = title
        self.description = description
        self.status = status

    def __str__(self):
        return f"{self.title} ({self.status}) - {self.description}"
