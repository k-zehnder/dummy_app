from flask import render_template, flash, redirect, url_for, current_app, make_response, request
from flask_migrate import current

from app import db
from app.models import Admin, User, Number, Task
from app.main import bp

@bp.route('/')
def index():
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
    return render_template('index.html', route_info=routes)

# @bp.route('/')
# def index():
#     admin = Admin.query.first()
#     admin.launch_task(name="test_task", description="desc")
#     print([i.complete for i in admin.tasks])
#     # return render_template('index.html')
#     return make_response("<h1>Hello IVR Team:))</h1>")
