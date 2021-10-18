from app import db

class User(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  username = db.Column(db.String(124), unique=True, nullable=False)
  
  numbers = db.relationship('Number', backref='user', lazy='dynamic')
  
  def __repr__(self):
    return '<User {}>'.format(self.username)


class Number(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  digits = db.Column(db.Integer, nullable=False, unique=True)
# (??)timezone = db.Column(function for finding timezone from number)

  user_id = db.Column(db.ForeignKey('user.id'))

  def __repr__(self):
    return '<Number {}>'.format(self.digits)

# https://stackoverflow.com/questions/46430061/flask-database-migrations-on-heroku
#
  # You actually want to do flask db init and flask db migrate locally. Commit the results to your git repo. Then on Heroku, you only do the heroku run flask db upgrade