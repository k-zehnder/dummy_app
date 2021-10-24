import time
from app.models import Admin, Task
from app import create_app, db

app = create_app()
app.app_context().push()

def test_task(admin_id): #self.id
    # test = Task.query.filter_by(Task.id==admin_id)
    # mark_complete = Task.query.filter_by(Task.id==id)
    # mark_complete.completed = True
    for i in range(3):
        print(admin_id)
        time.sleep(2)

def background_task(n):

    """ Function that returns len(n) and simulates a delay """

    delay = 2

    print("Task running")
    print(f"Simulating a {delay} second delay")

    time.sleep(delay)

    print(len(n))
    print("Task complete")

    return len(n)