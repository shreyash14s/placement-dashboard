import config
from flask_sqlalchemy import SQLAlchemy
from app import fapp

fapp.config['SQLALCHEMY_DATABASE_URI'] = config.SQLALCHEMY_DATABASE_URI
db = SQLAlchemy(fapp)


# from sqlalchemy import create_engine
# from sqlalchemy.orm import scoped_session, sessionmaker
# from sqlalchemy.ext.declarative import declarative_base

# engine = create_engine(config.SQLALCHEMY_DATABASE_URI, convert_unicode=True)
# db_session = scoped_session(sessionmaker(autocommit=False,
#                                          autoflush=False,
#                                          bind=engine))

# Base = declarative_base()
# Base.query = db_session.query_property()

def init_db():
    # import all modules here that might define models so that
    # they will be registered properly on the metadata. Otherwise
    # you will have to import them first before calling init_db()
    import app.models
    # Base.metadata.create_all(bind=engine)
    # db.drop_all()
    db.create_all()

def load_data():
    import app.controller as control
    import csv

    init_db()

    fieldnames = ("name", "usn", "stream", "age", "per10", "per12", "cgpa", "email", "resume")
    with open('../studentsdata.csv') as f:
        for row in csv.DictReader(f, fieldnames):
            control.add_student(**row)
