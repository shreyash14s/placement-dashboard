import enum,os
from openpyxl import Workbook
from flask import Flask,send_from_directory
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer, String, Float, CheckConstraint, \
    Enum, Date, ForeignKey
from sqlalchemy.orm import relationship,load_only
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] ='sqlite:///C:\\sqlite\\placement.db'
#path to the current directory 
app.config['path'] = 'C:\\Users\\Sanjana Jairam\\AppData\\Local\\Programs\\Python\\Python35-32'
#app.config['SQLALCHEMY_ECHO'] = True
db = SQLAlchemy(app)


class Stream(enum.Enum):
    CSE = 'CSE'
    IS = 'IS'
    EEE = 'EEE'
    ECE = 'ECE'
    EME = 'EME'
    EBT = 'EBT'
    ECV = 'ECV'
    MBA = 'MBA'
    BBA = 'BBA'
    
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

    def __init__(self, name=None, usn=None, stream=None, age=None, tenth=None, \
            twelfth=None, cgpa=None, email=None, resume=None):
        self.name = name
        self.usn = usn
        self.stream = stream
        self.age = age
        self.tenth_percentage = tenth
        self.twelfth_percentage = twelfth
        self.cgpa = cgpa
        self.email_id = email
        self.resume_link = resume

    def __repr__(self):
        return '%s, %s, %s, %.2f, %.2f, %.2f' % (self.usn, self.name, self.email_id, self.tenth_percentage,self.twelfth_percentage,self.cgpa) 

class Company(db.Model):
    __tablename__ = 'company'
    name = Column(String(120), nullable=False)
    company_id = Column(Integer, primary_key=True)
    test_date = Column(Date, nullable=False)
    interview_date = Column(Date, nullable=False)
    tier = Column(Integer, CheckConstraint('tier>=1 and tier<=3'))
    website = Column(String(320))
    postal_address = Column(String(500))
    company_sector = Column(String(50))

    def __init__(self, name=None, company_id=None, test_date=None, interview_date=None, \
            tier=None, company=None, website=None, postal_address=None, company_sector=None):
        self.name = name
        self.company_id = company_id
        self.test_date = test_date
        self.interview_date = interview_date
        self.tier = tier
        self.company = company
        self.website = website
        self.postal_address = postal_address
        self.company_sector = company_sector

    def __repr__(self):
        return '%d ,%s' % (self.company_id, self.name)


class Registrations(db.Model):
    __tablename__ = 'registrations'
    usn = Column(String(15), ForeignKey('student.usn'), primary_key=True, nullable=False)
    company_id = Column(Integer, ForeignKey('company.company_id'), primary_key=True)

    student = relationship('Student', foreign_keys='Registrations.usn')
    company = relationship('Company', foreign_keys='Registrations.company_id')

    def __init__(self, usn=None, company_id=None):
        self.usn = usn
        self.company_id = company_id

    def __repr__(self):
        return 'Company %s =  %s' % (self.company_id,self.usn)

db.create_all()


@app.route("/generate/<comp_name>", methods=['GET'])
def gen_excel_sheets(comp_name):
	filename = comp_name+".xlsx"
	wb = Workbook()
	ws = wb.active
	ws.title = comp_name
	header = ['USN','Name','Email-ID','10th %','12th/Diploma %','CGPA %']
	ws.append(header)
	company = Company.query.filter_by(name=comp_name).with_entities(Company.company_id).first()
	usn = Registrations.query.filter_by(company_id=company[0]).with_entities(Registrations.usn).all()
	for u in usn:
		q = Student.query.get(str(u[0]))
		stud_details = str(q).split(',')
		ws.append(stud_details)
	wb.save(filename)
	return send_from_directory(app.config['path'],filename,as_attachment=True)

