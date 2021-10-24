from flask import render_template, flash, redirect, url_for, current_app, make_response, request
from flask_migrate import current

from app import db
from app.models import Admin, User, Number, Task
from app.main import bp

@bp.route('/')
def index():
    admin = Admin.query.first()
    admin.launch_task(name="test_task", description="desc")
    print([i.complete for i in admin.tasks])
    return f"<h1>Hello IVR Team :))</h1>"

@bp.route('/users')
def users_boot():
    users = User.query.all()
    users = [user.to_dict() for user in users]
    # other column settings -> http://bootstrap-table.wenzhixin.net.cn/documentation/#column-options
    columns = [
    {
        "field": "username", # which is the field's name of data key 
        "title": "username", # display as the table header's name
        "sortable": True,
    }]
    return render_template('boot_table_non_miguel.html', title='Users', data=users, columns=columns)

@bp.route('/users_ajax')
def users():
    return render_template('ajax_table.html', title='Users')

