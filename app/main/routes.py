from flask import render_template, flash, redirect, url_for, current_app

from app import db
from app.models import User, Number
from app.main import bp

@bp.route('/users')
def users():
    return render_template('ajax_table.html', title='Users')

