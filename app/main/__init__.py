from flask import Blueprint

bp = Blueprint('main', __name__)

# must go down here to prevent circlar import
from app.main import routes