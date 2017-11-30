from app.models import StudentUser, PlacementUser, Company, Registrations, Student, Offered
from app.database import db
from datetime import date
from config import CSV_URL
import requests
import csv
import json
import io

def signup_student(user, pwd):
    '''
    Create new student user.
    '''
    pass

def login_student(user, pwd):
    '''
    Returns True if the username and password match.
    '''
    s = StudentUser.query.filter_by(usn=user.upper()).first()
    if s:
        return s.password == pwd
    return False

def get_all_companies():
    comp = Company.query.filter(Company.register_date>=date.today()).order_by(Company.company_id).all()
    l = []
    for q in comp:
        comp_details = {
            'name': q.name, 'company_id': q.company_id,
            'register_date': q.register_date, 'cutoff_gpa': q.cutoff_gpa,
            'test_date': q.test_date, 'interview_date': q.interview_date,
            'tier': q.tier, 'website': q.website,
            'postal_address': q.postal_address, 'company_sector': q.company_sector
        }
        l.append(comp_details)
    return l

def get_student_details(usn):
    q = Student.query.get(usn)
    stud_details = [q.usn, q.name, q.email_id, q.tenth_percentage, q.twelfth_percentage, q.cgpa]
    return stud_details

def register_for(usn, company_id):
    '''
    Register the student for company.
    '''
    r = Registrations(usn=usn, company_id=company_id)
    db.session.add(r)
    db.session.commit()

# def update_student_details(usn):
#     '''
#     Sends true if update successful.
#     '''
#     pass
# def update_student_password(usn,password):
#     '''
#     Sends true if update successful.
#     '''
#     pass

def get_student_status(usn):
    stat = Offered.query.filter_by(usn=usn)
    data = []
    for q in stat:
        r = {}
        qname = Company.query.get(q.company_id)
        r["Name"] = qname.name
        role = q.role
        r["Role"] = str(role)
        data.append(r)
    # data[usn] = r
    return data

# def ask_placementuser(usn, question):
#     '''
#     Record Question if the student has any
#     '''
#     pass

def login_placementuser(name,password):
    '''
    Sends true if login successful.
    '''
    s = PlacementUser.query.filter_by(name=name)
    if s:
        return s.password == password
    return False

def add_company(name, company_id, cutoff_gpa, register_date, test_date, interview_date, tier, website, postal_address, company_sector):
    c = Company(name=name, company_id=company_id,cutoff_gpa=cutoff_gpa, test_date=test_date,register_date=register_date,interview_date=interview_date, tier=tier,website=website, postal_address=postal_address, company_sector=company_sector)
    db.session.add(c)
    db.session.commit()

def remove_company(name, company_id, test_date, interview_date, \
            tier, company, website, postal_address, company_sector):
    '''
    Note ***** Add the cutoff cgpa parameter
    Sends true if company is removed successfuly.
    '''
    pass

def remove_student(usn):
    s = Student.query.filter_by(usn=usn)
    if s:
        s.delete()
        db.session.commit()
    return "Student deleted"

def make_announcement(message):
    '''
    Allows the placement user to make announcement to all the students
    '''
    l = list(map(lambda x: x[0], Student.query.with_entities(Student.name).all()))
    with open('emails.txt', 'w') as f:
        print(','.join(l), file=f)
    # call_php()

def is_in_db(usn):
    s = Student.query.filter_by(usn=usn.upper()).first()
    if s:
        return True
    return False

def get_new_registrants():
    '''
    Get new registrants for verification.
    '''
    d = requests.get(CSV_URL)
    # Timestamp	Name	USN	Stream	Age	10th percentage	12th percentage	CGPA Score	Email ID	Resume Link
    fieldnames = ("timestamp", "name", "usn", "stream", "age", "per10", "per12", "CGPA", "email_id", "resume_link")
    l = []
    reader = csv.DictReader(io.StringIO(d.text), fieldnames)
    for row in reader:
        if not is_in_db(row['usn'].upper()):
            l.append(row)
    return l[1:]

def add_student(usn, name, stream, age, per10, per12, cgpa, email, resume):
    age = int(age)
    per10 = float(per10)
    per12 = float(per12)
    cgpa = float(cgpa)
    s = Student(usn=usn, name=name, stream=stream, age=age, tenth=per10, 
                twelfth=per12, cgpa=cgpa, email=email, resume=resume)
    db.session.add(s)
    db.session.commit()
