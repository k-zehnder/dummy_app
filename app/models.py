from flask import current_app
from app import db
import rq
import redis

class Admin(db.Model):
  id = db.Column(db.Integer, nullable=False, primary_key=True)
  name = db.Column(db.String(124), nullable=False, unique=True)
  team = db.Column(db.String(124), nullable=True, unique=False)
  
  tasks = db.relationship('Task', backref='admin',lazy='dynamic')

  def launch_task(self, name, description, *args, **kwargs):
      rq_job = current_app.task_queue.enqueue(f'app.tasks.{name}', self.id, *args, **kwargs)
      task = Task(id=rq_job.get_id(), name=name, description=description,
                  admin=self)
      db.session.add(task)
      db.session.commit() #why miguel not have this? b/c its in /export_posts route?
      return task

  def to_dict(self):
    return {"name" : self.name}

  def from_dict(self, input_dict):
    for field in ["name", "team"]:
      if field in input_dict:
        setattr(self, field, input_dict[field])

  def __repr__(self):
    return f"<Admin {self.name}>"

class User(db.Model):
  id = db.Column(db.Integer, nullable=False, primary_key=True)
  username = db.Column(db.String(124), unique=True, nullable=False)
  
  numbers = db.relationship('Number', backref='user', lazy='dynamic')

  def to_dict(self):
    return {'username': self.username}

  def from_dict(self, data):
    for field in ['username']:
        if field in data:
            setattr(self, field, data[field])

  def __repr__(self):
    return f"<User {self.username}>"

class Number(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  digits = db.Column(db.String(124), nullable=False, unique=False)

  user_id = db.Column(db.ForeignKey('user.id'))

  def __repr__(self):
    return f"<Number {self.digits}>"

class Task(db.Model):
    id = db.Column(db.String(500),primary_key=True)
    name = db.Column(db.String(128))
    description = db.Column(db.String(128))
    complete = db.Column(db.Boolean, default=False)

    admin_id = db.Column(db.ForeignKey('admin.id'))

    def get_rq_job(self):
        try:
            rq_job = rq.job.Job.fetch(self.id, connection=current_app.redis)
        except (redis.exceptions.RedisError, rq.exceptions.NoSuchJobError):
            return None
        return rq_job

    def get_progress(self):
        job = self.get_rq_job()
        return job.meta.get('progress', 0) if job is not None else 100

# https://stackoverflow.com/questions/46430061/flask-database-migrations-on-heroku
#
  # You actually want to do flask db init and flask db migrate locally. Commit the results to your git repo. Then on Heroku, you only do the heroku run flask db upgrade