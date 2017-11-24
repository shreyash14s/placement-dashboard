from sqlalchemy import Column, Integer, String, Float, CheckConstraint, Enum
from app.database import Base

class Student(Base):
    __tablename__ = 'student'
    name = Column(String(320), nullable=False)
    usn = Column(String(120))

    def __init__(self, name=None, usn=None):
        self.name = name
        self.usn = usn

    def __repr__(self):
        return '<User %r>' % (self.name)

class CGPAList(Base):
    __tablename__ = 'cgpa_list'
    usn = Column(String(15), nullable=False)
    cgpa = Column(Float, CheckConstraint('cgpa>0 and cgpa<=10'))

    def __init__(self, usn=None, cgpa=None):
        self.usn = usn
        self.cgpa = cgpa

    def __repr__(self):
        return '<CGPA %s = %s>' % (self.usn, self.cgpa)
