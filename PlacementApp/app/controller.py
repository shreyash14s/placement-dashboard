from app.models import StudentUser
from app.models import PlacementUser
from app.models import Company, Registrations, Student
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
    q = Company.query.order_by(Company.company_id).all()
    comp_details = [q.name, q.company_id, q.register_date,q.cutoff_gpa, q.test_date, q.interview_date, q.tier, q.company, q.website, q.postal_address, q.company_sector ]
    return comp_details
    
def get_student_details(usn):
    q = Student.query.get(usn)
    stud_details = [q.usn, q.name, q.email_id, q.tenth_percentage, q.twelfth_percentage, q.cgpa]
    return stud_details

def register_for(usn, company_id):
    '''
    Register the student for company.
    '''
    pass
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
def  get_student_status(usn):
    '''
    return all possible companies a student has been offered job in.
    '''
    pass
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
def add_company(name, company_id, test_date, interview_date, \
            tier, company, website, postal_address, company_sector):
    '''
    Note ***** Add the cutoff cgpa parameter
    Sends true if company is added successfuly.
    '''
    pass
def remove_company(name, company_id, test_date, interview_date, \
            tier, company, website, postal_address, company_sector):
    '''
    Note ***** Add the cutoff cgpa parameter
    Sends true if company is removed successfuly.
    '''
    pass
def remove_student(usn):
     Student.query.filter_by(Student.usn=usn).delete()
     return "Student deleted"

def make_announcement(message):
    '''
    Allows the placement user to make announcement to all the students
    '''
    pass
