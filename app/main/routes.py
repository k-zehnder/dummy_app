from flask import render_template

from app import db
from app.models import Admin, User, Number, Task
from app.main import bp
from multiprocessing import Value

counter = Value('i', 0)

@bp.route('/')
def index():
    # NOTE: this is broken. "resets" on each user session I think.
    with counter.get_lock():
        counter.value += 1
        # save the value ASAP rather than passing to jsonify
        # to keep lock time short
        unique_count = counter.value
    admin = Admin.query.first()
    admin.launch_task(name="test_task", description="desc")
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
    return render_template('index.html', route_info=routes, counter=unique_count)


@bp.route('/test_route')
def test_route():
    return render_template("test.html")
