from flask import Blueprint

bp = Blueprint('api', __name__)

# must go down here to prevent circlar import
from app.api import routes