from app import fapp
from app.query import gen_excel_sheets
from app.controller import login_student, login_placementuser, register_for, get_student_details, remove_student, get_all_companies, get_student_status
from app.views_placement import login_required_placement
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
# @login_required_student
def register_company():
    usn = request.args.get('usn')
    company_id = request.args.get('company_id')
    register_for(usn, company_id)
    # if usn and company_id and usn == session['username']:
    #     try:
    #         register_for(usn, company_id)
    #         flash('Successfully registered!')
    #     except:
    #         flash('Failed to register')
    # return redirect(url_for('dashboard'))
    return 'ok'

@fapp.route("/dashboard/student_details/<usn>", methods=['GET'])
@login_required_student
def get_student_details_view(usn):
    details = get_student_details(usn)
    return str(details)

@fapp.route("/dashboard/get_stud_status/<usn>", methods=['GET'])
# @login_required_placement
def get_stud_status(usn):
    stat = get_student_status(usn)
    return str(stat)

@fapp.route("/dashboard/get_companies", methods=['GET'])
# @login_required_student
def get_companies():
    comp_details = get_all_companies()
    return str(comp_details)
     
@fapp.route("/dashboard/add_company", methods=['GET'])
def add_comp():
    name = request.args.get('name')
    company_id = request.args.get('company_id')
	cutoff_gpa = request.args.get('cutoff_gpa')
	register_date = request.args.get('register_date ')
	test_date = request.args.get('test_date')
	interview_date = request.args.get('interview_date')
	tier = request.args.get('tier')
	website = request.args.get('website')
	postal_address = request.args.get('postal_address')
	company_sector = request.args.get('company_sector')
	
    add_company(name, company_id, cutoff_gpa, register_date, test_date, interview_date, tier, website,\ postal_address, company_sector)
