from persistence_sqlite import get_tasks, save_task, update_task, init_storage

def setup_system():
    init_storage()

def get_all_tasks():
    return get_tasks()

def create_task(title, description):
    return save_task(title, description)

# NB: task number er 1-baseret
def mark_done(task_number):
    update_task(get_tasks()[task_number -1], 'done')

setup_system()
create_task('coffee', 'brew coffee')
create_task('code', 'write code')
print(get_all_tasks())
