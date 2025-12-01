import pytest
from flask import Flask

import task_manager
import persistence_sqlite as persistence_mock
app = Flask(__name__)

@pytest.fixture(autouse=True)
def reset_data():
    persistence_mock._tasks.clear()
    yield
    persistence_mock._tasks.clear()

def test_create_task():
    task_manager.create_task("Kaffe", "Lav en kop kaffe")
    tasks = persistence_mock.get_tasks()
    assert len(tasks) == 1
    assert tasks[0].title == "Kaffe"

def test_mark_done():
    task_manager.add_task("Mail", "Svar")
    task_manager.mark_done(1)
    tasks = persistence_mock.get_tasks()
    assert tasks[0].status == "done"
