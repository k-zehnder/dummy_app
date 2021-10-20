from app import db

class User(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  username = db.Column(db.String(124), unique=True, nullable=False)
  
  numbers = db.relationship('Number', backref='user', lazy='dynamic')

  def to_dict(self):
    return {
          'username': self.username,
        }

  def from_dict(self, data):
    for field in ['username']:
        if field in data:
            setattr(self, field, data[field])

  def __repr__(self):
    return '<User {}>'.format(self.username)


class Number(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  digits = db.Column(db.String(124), nullable=False, unique=False)

  user_id = db.Column(db.ForeignKey('user.id'))

  def __repr__(self):
    return '<Number {}>'.format(self.digits)


# class Task(db.Model):
#   pass

# class Order(db.Model):
#   pass

# class Product(db.Model):
#   pass

# class Notification(db.Model):
#   pass

# https://stackoverflow.com/questions/46430061/flask-database-migrations-on-heroku
#
  # You actually want to do flask db init and flask db migrate locally. Commit the results to your git repo. Then on Heroku, you only do the heroku run flask db upgrade