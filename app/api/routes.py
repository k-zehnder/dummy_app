from flask import current_app

from app import db
from app.models import User, Number
from app.api import bp

@bp.route('/api/data')
def data():
    return {'data': [user.to_dict() for user in User.query]}
