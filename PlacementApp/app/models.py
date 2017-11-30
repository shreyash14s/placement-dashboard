import enum
from sqlalchemy import Column, Integer, String, Float, CheckConstraint, \
    Enum, Date, ForeignKey
from sqlalchemy_utils.types.choice import ChoiceType
from sqlalchemy_utils.types.password import PasswordType
from sqlalchemy.orm import relationship
# from app.database import Base
from app.database import db
# from sqlalchemy.schema import CreateTable
# import sqlalchemy.dialects.mysql as mysql

# Enum = db.Enum
# Column = db.Column
# String = db.String

class Stream(enum.Enum):
    CSE = 'CSE'
    IS = 'IS'
    EEE = 'EEE'
    ECE = 'ECE'
    EME = 'EME'
    BT = 'BT'
    CV = 'CV'
    BBA = 'BBA'
    MBA = 'MBA'

class Student(db.Model):
    __tablename__ = 'student'
    name = Column(String(120), nullable=False)
    usn = Column(String(15), primary_key=True)
    stream = Column(Enum(Stream))
    age = Column(Integer, CheckConstraint('age > 18'))
    tenth_percentage = Column(Float, CheckConstraint('tenth_percentage>=0 and tenth_percentage<=100'))
    twelfth_percentage = Column(Float, CheckConstraint('tenth_percentage>=0 and tenth_percentage<=100'))
    cgpa = Column(Float, CheckConstraint('cgpa>0 and cgpa<=10.0'))
    email_id = Column(String(50), nullable=False)
    resume_link = Column(String(320))
    status_placed = Column(String(4))
    def __init__(self, name=None, usn=None, stream=None, age=None, tenth=None, \
            twelfth=None, cgpa=None, email=None, resume=None, status=None):
        self.name = name
        self.usn = usn
        self.stream = stream
        self.age = age
        self.tenth_percentage = tenth
        self.twelfth_percentage = twelfth
        self.cgpa = cgpa
        self.email_id = email
        self.resume_link = resume
        self.status_placed = status
    def __repr__(self):
        return '<User %r, %s>' % (self.name, self.usn)

# print(CreateTable(Student.__table__).compile(dialect=mysql.dialect()))

class Company(db.Model):
    __tablename__ = 'company'
    name = Column(String(120), nullable=False)
    company_id = Column(Integer, primary_key=True)
    cutoff_gpa = Column(Float, CheckConstraint('cutoff_gpa>=0 and cutoff_gpa<=10'))
    register_date = Column(Date, nullable=False)
    test_date = Column(Date, nullable=False)
    interview_date = Column(Date, nullable=False)
    tier = Column(Integer, CheckConstraint('tier>=1 and tier<=3'))
    website = Column(String(320))
    postal_address = Column(String(500))
    company_sector = Column(String(50))

    def __init__(self, name=None, company_id=None,cutoff_gpa=None, test_date=None, interview_date=None, \
            tier=None, company=None, website=None, postal_address=None, company_sector=None):
        self.name = name
        self.company_id = company_id
        self.cutoff_gpa = cutoff_gpa
        self.test_date = test_date
        self.interview_date = interview_date
        self.tier = tier
        self.company = company
        self.website = website
        self.postal_address = postal_address
        self.company_sector = company_sector
        
    def __repr__(self):
        return '<Company %s>' % (self.name)

# print(CreateTable(Company.__table__).compile(dialect=mysql.dialect()))

class Registrations(db.Model):
    __tablename__ = 'registrations'
    usn = Column(String(15), ForeignKey('student.usn'), primary_key=True, nullable=False)
    company_id = Column(Integer, ForeignKey('company.company_id'), primary_key=True)

    student = relationship('Student', foreign_keys='Registrations.usn')
    company = relationship('Company', foreign_keys='Registrations.company_id')

    def __init__(self, usn=None, cgpa=None):
        self.usn = usn
        self.cgpa = cgpa

    def __repr__(self):
        return '<CGPA %s = %s>' % (self.usn, self.cgpa)

# print(CreateTable(Registrations.__table__).compile(dialect=mysql.dialect()))

# class CGPAList(db.Model):
#     __tablename__ = 'cgpa_list'
#     usn = Column(String(15), nullable=False)
#     cgpa = Column(Float, CheckConstraint('cgpa>0 and cgpa<=10'))

#     def __init__(self, usn=None, cgpa=None):
#         self.usn = usn
#         self.cgpa = cgpa

#     def __repr__(self):
#         return '<CGPA %s = %s>' % (self.usn, self.cgpa)

class StudentUser(db.Model):
    __tablename__ = 'student_user'
    usn = Column(String(15), ForeignKey('student.usn'), primary_key=True, nullable=False)
    password = Column(PasswordType(
            schemes=[
                'pbkdf2_sha512'
            ]
        ))

    student = relationship('Student', foreign_keys='StudentUser.usn')

    def __init__(self, usn=None, passwd=None):
        self.usn = usn
        self.password = passwd

    def __repr__(self):
        return '<StudentUser %s>' % (self.usn)

    def is_authenticated(self):
        return True
 
    def is_active(self):
        return True
 
    def is_anonymous(self):
        return False
 
    def get_id(self):
        # return unicode(self.id)
        return self.usn

class PlacementUser(db.Model):
    __tablename__ = 'placement_user'
    name = Column(String(20), primary_key=True, nullable=False)
    password = Column(PasswordType(
            schemes=[
                'pbkdf2_sha512'
            ]
        ))
    
    def __init__(self, name=None, passwd=None):
        self.name = name
        self.password = passwd

    def __repr__(self):
        return '<PlacementUser %s>' % (self.usn)

class Role(enum.Enum):
    FTE_INT = 0
    FTE = 1
    INT = 2
    INT_2 = 3

class Offered(db.Model):
    __tablename__ = 'offered'
    usn = Column(String(15), ForeignKey('student.usn'), primary_key=True, nullable=False)
    company_id = Column(Integer, ForeignKey('company.company_id'), primary_key=True)
    role = Column(Enum(Role))
    
    def __init__(self, usn=None, company_id=None, role=None):
        self.usn = usn
        self.company_id = company_id
        self.role = role

    def __repr__(self):
        return '<PlacementUser %s>' % (self.usn)
