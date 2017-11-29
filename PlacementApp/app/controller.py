from app.models import StudentUser
from app.models import PlacementUser
def signup_student(user, pwd):
    '''
    Create new student user.
    '''
    pass

def login_student(user, pwd):
    '''
    Returns True if the username and password match.
    '''
    pass

def get_all_companies():
    '''
    Returns all the companies list available for registration.
    '''
    pass

def get_student_details(usn):
    '''
    Returns the student details.
    '''
    pass

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
def remove_studet(usn):
    ''' 
    PlacementUSer can remove a student if they want to block him
    '''
    pass
def make_announcement(message):
    '''
    Allows the placement user to make announcement to all the students
    '''
    pass
