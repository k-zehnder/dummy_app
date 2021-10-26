from flask import jsonify, request, url_for, abort, current_app, render_template
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

user = api.model('User', {
    'id': fields.String(required=True, description='The user identifier'),
    'username': fields.String(required=True, description='The username'),
})


@api.route('/cats')
class CatList(Resource):
    @api.doc('list_cats')
    @api.marshal_list_with(cat)
    def get(self):
        '''List all cats'''
        return CATS

@api.route('/users')
class UsersList(Resource):
    @api.doc('list_users')
    @api.marshal_list_with(user)
    def get(self):
        '''List all users'''
        return User.query.all()

    def post(self):
        pass


@bp.route('/users', methods=['GET'])
def users_get():
    return {'data': [user.to_dict() for user in User.query]}

@bp.route('/users', methods=['POST'])
def users_post():
    data = request.form.to_dict() or {}   
    user = User(username=data["username"])
    #user.from_dict(data)
    db.session.add(user)
    db.session.commit()
    response = jsonify(user.to_dict())
    return response

@bp.route('/get_user__by_id/<int:id>', methods=['GET'])
def get_user_by_id(id):
    return jsonify(User.query.get_or_404(id).to_dict())

@bp.route('/bootstrap_table')
def bootstrap_table():
    data = [user.to_dict() for user in User.query]
    # other column settings -> http://bootstrap-table.wenzhixin.net.cn/documentation/#column-options
    columns = [
    {
        "field": "username", # which is the field's name of data key 
        "title": "name", # display as the table header's name
        "sortable": True,
    }]
    return render_template("boot_table_non_miguel.html",
      data=data,
      columns=columns,
      title='Flask Bootstrap Table')

@bp.route('/users_ajax')
def users():
    return render_template('ajax_table.html', title='Users')