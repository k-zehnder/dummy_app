from flask import render_template, flash, redirect, url_for, current_app

from app import db
from app.models import User, Number
from app.main import bp

@bp.route('/')
def index():
    return "<h1>Hello IVR Team :)</h1>"

@bp.route('/users_boot')
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
    return render_template('nomiguel.html', title='Users', data=users, columns=columns)

@bp.route('/users')
def users():
    return render_template('ajax_table.html', title='Users')

