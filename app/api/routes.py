from flask import jsonify, request, url_for, abort, current_app
from flask_restx import Namespace, Resource, fields

from app import db
from app.models import User, Number
from app.api import bp
from flask_restx import Namespace, Resource, fields
from app.api import api

cat = api.model('Cat', {
    'id': fields.String(required=True, description='The cat identifier'),
    'name': fields.String(required=True, description='The cat name'),
})


CATS = [
    {'id': 'felix', 'name': 'Felix'},
]

@api.route('/cats')
class CatList(Resource):
    @api.doc('list_cats')
    @api.marshal_list_with(cat)
    def get(self):
        '''List all cats'''
        return CATS

@bp.route('/users', methods=['GET'])
def data():
    return {'data': [user.to_dict() for user in User.query]}

@bp.route('/users', methods=['POST'])
def create_user():
    data = request.form.to_dict() or {}   
    user = User(username=data["username"])
    #user.from_dict(data)
    db.session.add(user)
    db.session.commit()
    response = jsonify(user.to_dict())
    return response

@bp.route('/users/<int:id>', methods=['GET'])
def get_user(id):
    return jsonify(User.query.get_or_404(id).to_dict())
