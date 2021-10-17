from flask import render_template, flash, redirect, url_for, current_app

from app import db
from app.models import User
from app.main import bp

@bp.route("/")
def index():
    return "<h1>hello IVR team</h1>"

@bp.route("/users")
def users():
    users = User.query.all()
    return f"<h3>one user\nusername: {users[0].username}"