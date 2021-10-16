from app import db

class User(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  username = db.Column(db.String(124), unique=True, nullable=False)
  
  #numbers = db.relationship('Number', backref='user', lazy='dynamic')

def __repr__(self):
    return f"User created: {self.username}"


# class Number(db.Model):
#   id = db.Column(db.Integer, primary_key=True)
#   digits = db.Column(db.Integer, nullable=False, unique=True)
# (??)timezone = db.Column(function for finding timezone from number)

#   user_id = db.Column(db.Foreigney('user.id'))


# def __repr__(self):
#   return f"Number created: {self.id, self.number}"