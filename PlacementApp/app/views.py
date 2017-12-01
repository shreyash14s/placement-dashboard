from app import fapp
from app.query import gen_excel_sheets
# from app.controller import login_student, login_placementuser, register_for, get_student_details, remove_student, get_all_companies
import app.controller as control
from app.views_placement import login_required_placement
from flask import send_from_directory, render_template, flash, redirect, \
        url_for, session, request
# from flask.ext.login import login_user, logout_user, current_user, login_required
from functools import wraps
import json

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
    return render_template('index.html')
    # return render_template('index.html')

@fapp.route('/dashboard')
@login_required_student
def dashboard():
    return render_template('dashboard.html')

@fapp.route('/companies.html')
@login_required_student
def companies():
    return render_template('companies.html')

# @fapp.route('/dashboard')
# def dashboard():
#     return render_template('dashboard.html')

@fapp.route('/login', methods=['POST'])
def login():
    username = request.form['username'].upper()
    password = request.form['password']
    # registered_user = User.query.filter_by(username=username,password=password).first()
    # if registered_user is None:
    if not control.login_student(username, password):
        flash('Username or Password is invalid', 'error')
        return redirect(url_for('index'))
    # login_user(registered_user)
    session['username'] = username
    session['logged_in'] = True
    flash('Logged in successfully')
    return redirect(request.args.get('next') or url_for('dashboard'))

@fapp.route('/dashboard/register_for', methods=['POST'])
# @login_required_student
def register_company():
    # usn = request.args.get('usn').upper()
    usn = session['username']
    company_id = request.args.get('company_id')
    control.register_for(usn, company_id)
    # if usn and company_id and usn == session['username']:
    #     try:
    #         register_for(usn, company_id)
    #         flash('Successfully registered!')
    #     except:
    #         flash('Failed to register')
    # return redirect(url_for('dashboard'))
    return 'ok'

@fapp.route("/dashboard/student_details/<usn>", methods=['GET'])
# @login_required_student
def get_student_details_view(usn):
    details = control.get_student_details(usn)
    return json.dumps(details)

@fapp.route("/dashboard/get_stud_status/<usn>", methods=['GET'])
# @login_required_placement
def get_stud_status(usn):
    stat = control.get_student_status(usn)
    return json.dumps(stat)

@fapp.route("/dashboard/get_companies", methods=['GET'])
# @login_required_student
def get_companies():
    #single quotes isnt json need double quotes strictly
    #also need to remove date type

    comp_details = control.get_all_companies()
    
    for x in comp_details:
        x.pop('test_date')
        x.pop('interview_date')
        x.pop('register_date')
    # comp_details=str(comp_details).replace("\'","\"")
    # return str(comp_details) 
    return json.dumps(comp_details)

# add_company(name,company_id , cutoff_gpa, register_date, test_date, interview_date, tier, website, postal_address, company_sector)
@fapp.route("/dashboard/get_statistics", methods=['GET'])
def get_statistics():
    stats = control.get_stats()
    return str(stats)
