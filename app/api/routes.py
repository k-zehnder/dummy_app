from flask import jsonify, request, url_for, abort, current_app

from app import db
from app.models import User, Number
from app.api import bp

@bp.route('/api/v1/users', methods=['GET'])
def data():
    return {'data': [user.to_dict() for user in User.query]}

@bp.route('/api/v1/users', methods=['POST'])
def create_user():
    data = request.form.to_dict() or {}   
    user = User(username=data["username"])
    #user.from_dict(data)
    db.session.add(user)
    db.session.commit()
    response = jsonify(user.to_dict())
    return response

@bp.route('/api/v1/users/<int:id>', methods=['GET'])
def get_user(id):
    return jsonify(User.query.get_or_404(id).to_dict())
