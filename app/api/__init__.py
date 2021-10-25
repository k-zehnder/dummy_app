from flask import Blueprint
from flask_restx import Api, Namespace


bp = Blueprint('api', __name__)
api = Api(bp, version='1.0', title='Todo API',
    description='A simple TODO API',
    default='API Default',
    default_label='API Default Label'
)
ns1 = Namespace('Cat')
api.add_namespace(ns1)

# must go down here to prevent circlar import
from app.api import routes