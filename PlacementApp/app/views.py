from app import fapp
from app.query import gen_excel_sheets
from app.controller import login_student, login_placementuser, register_for, get_student_details
from flask import send_from_directory, render_template, flash, redirect, \
        url_for, session, request
# from flask.ext.login import login_user, logout_user, current_user, login_required
from functools import wraps

def login_required_student(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        if 'logged_in' in session:
            return f(*args, **kwargs)
        else:
            flash("Please Log In")
            return redirect(url_for('index'))
    return wrap

@fapp.route('/')
def index():
    return render_template('dashboard.html')
    # return render_template('index.html')

# @fapp.route('/dashboard')
# def dashboard():
#     return render_template('dashboard.html')

@fapp.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']
    # registered_user = User.query.filter_by(username=username,password=password).first()
    # if registered_user is None:
    if not login_student(username, password):
        flash('Username or Password is invalid', 'error')
        return redirect(url_for('index'))
    # login_user(registered_user)
    session['username'] = username
    session['logged_in'] = True
    flash('Logged in successfully')
    return redirect(request.args.get('next') or url_for('dashboard'))

@fapp.route('/dashboard')
@login_required_student
def dashboard():
    return render_template('sidebar.html')

@fapp.route('/dashboard/register_for', methods=['GET'])
@login_required_student
def register_company():
    usn = request.args.get('usn')
    company_id = request.args.get('company_id')
    if usn and company_id and usn == session['username']:
        try:
            register_for(usn, company_id)
            flash('Successfully registered!')
        except:
            flash('Failed to register')
    return redirect(url_for('dashboard'))

@fapp.route('/dashboard/register_for', methods=['GET'])
@login_required_student
def register_company():
    usn = request.args.get('usn')
    company_id = request.args.get('company_id')
    if usn and company_id and usn == session['username']:
        try:
            register_for(usn, company_id)
            flash('Successfully registered!')
        except:
            flash('Failed to register')
    return redirect(url_for('dashboard'))

@fapp.route("/dashboard/student_details/<usn>", methods=['GET'])
@login_required_student
def get_student_details_view(usn):
    details = get_student_details(usn)
    return details
