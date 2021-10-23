from flask import Blueprint
from flask_restplus import Api, Namespace

ns1 = Namespace('users', description='users related operations')


bp = Blueprint('api', __name__, url_prefix="/doc")
api = Api(bp, version='1.0', title='Todo API',
    description='A simple TODO API',
)
api.add_namespace(ns1)


# must go down here to prevent circlar import
from app.api import routes