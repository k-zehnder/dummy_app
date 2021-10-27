from flask import render_template

from app import db
from app.models import Admin, User, Number, Task, ViewCount
from app.main import bp


@bp.route('/')
def index():
    admin = Admin.query.first()
    admin.launch_task(name="increment_viewcount", description="increment view counter += 1")
    counter = admin.views.counts
    routes = [
        {"id" : 1,
        "description" : "homepage with topology of routes",
        "blueprint" : "main",
        "link" : "main.index"},
        {"id" : 2,
        "description" : "flask-restx fully documented API",
        "blueprint" : "api",
        "link" : "api.doc"}
    ]
    return render_template('index.html', route_info=routes, counter=counter)


@bp.route('/test_route')
def test_route():
    return render_template("test.html")
