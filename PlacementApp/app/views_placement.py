'''
Placement views
'''
from app import fapp
from app.query import gen_excel_sheets
from app.controller import login_student, login_placementuser
from flask import send_from_directory, render_template, flash, redirect, \
        url_for, session, request
# from flask.ext.login import login_user, logout_user, current_user, login_required
from config import EXCEL_FILES_DIR
from functools import wraps


def login_required_placement(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        if 'logged_in_placement' in session:
            return f(*args, **kwargs)
        else:
            flash("Please Log In")
            return redirect(url_for('index'))
    return wrap

@fapp.route('/placement/login', methods=['POST'])
def placement_login():
    username = request.form['username']
    password = request.form['password']
    if not login_placementuser(username, password):
        flash('Username or Password is invalid', 'error')
        return redirect(url_for('index'))
    # login_user(registered_user)
    session['username'] = username
    session['logged_in_placement'] = True
    flash('Logged in successfully')
    return redirect(request.args.get('next') or url_for('placement_dashboard'))

@fapp.route('/placement/dashboard')
@login_required_placement
def placement_dashboard():
    return render_template('404.html') # Placement dashboard

@fapp.route("/placement/generate/<comp_id>", methods=['GET'])
@login_required_placement
def get_excel(comp_id):
    filename = gen_excel_sheets(comp_id)
    if filename:
        return send_from_directory(EXCEL_FILES_DIR, filename, as_attachment=True)
