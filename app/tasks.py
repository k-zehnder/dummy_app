import time
from app.models import Admin, Task
from app import create_app, db
from rq import get_current_job

app = create_app()
app.app_context().push()

def _set_task_progress(progress):
    job = get_current_job()
    if job:
        job.meta['progress'] = progress
        job.save_meta()
        task = Task.query.get(job.get_id())
        # task.user.add_notification('task_progress', {'task_id': job.get_id(),
        #                                              'progress': progress})
        if progress >= 100:
            task.complete = True
        db.session.commit()

def test_task(admin_id): #self.id
    admin = Admin.query.filter(Admin.id==admin_id).first()
    test = admin.tasks[0]
    _set_task_progress(0)
    print(f"test complete? {test.complete}")
    total = 3
    for i in range(total):
        print(f"progress: {100 * i // total}")
        time.sleep(2)
        _set_task_progress(100 * i // total)
    test.complete = True
    db.session.commit()
    _set_task_progress(100)
    print(f"test complete? {test.complete}")

