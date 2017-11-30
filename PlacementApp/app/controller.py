from json import dumps
from app.models import StudentUser
from app.models import PlacementUser
from app.models import Company, Registrations, Student, Offered
from app.database import db
def signup_student(user, pwd):
    '''
    Create new student user.
    '''
    pass

def login_student(user, pwd):
    '''
    Returns True if the username and password match.
    '''
    s = StudentUser.query.filter_by(usn=user)
    if s:
        return s.password == pwd
    return False

def get_all_companies():
    comp = Company.query.order_by(Company.company_id).all()
    l = []
    for q in comp:
		
        comp_details = [q.name, q.company_id, q.register_date, q.cutoff_gpa, q.test_date, q.interview_date, q.tier, q.website, q.postal_address, q.company_sector ]
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

def update_student_details(usn):
    '''
    Sends true if update successful.
    '''
    pass
def update_student_password(usn,password):
    '''
    Sends true if update successful.
    '''
    pass
def get_student_status(usn):
	stat = Offered.query.filter_by(usn=usn)
	data = {}
	for q in stat:
		r = {}
		qname = Company.query.get(q.company_id)
		r["Name"] = qname.name
		role = q.role
		r["Role"] = str(role)
	data[usn] = r
	return dumps(data) 
    
	
	
def ask_placementuser(usn,question):
    '''
    Record Question if the student has any
    '''
    pass
def  login_placementuser(name,password):
    '''
    Sends true if login successful.
    '''
    pass

def add_company(name, company_id, cutoff_gpa, register_date, test_date, interview_date, tier, website, postal_address, company_sector):
    c = Company(name=name, company_id=company_id,cutoff_gpa=cutoff_gpa, test_date=test_date,register_date=register_date,interview_date=interview_date, tier=tier,website=website, postal_address=postal_address, company_sector=company_sector)
    db.session.add(c)
    db.session.commit()

def remove_company(name, company_id, test_date, interview_date, 
            tier, company, website, postal_address, company_sector):
    '''
    Note ***** Add the cutoff cgpa parameter
    Sends true if company is removed successfuly.
    '''
    pass
def remove_student(usns):
    
	pass
def make_announcement(message):
    '''
    Allows the placement user to make announcement to all the students
    '''
    pass
