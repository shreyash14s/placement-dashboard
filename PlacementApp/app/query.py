import os
from openpyxl import Workbook
from app.models import Company, Registrations, Student
from config import EXCEL_FILES_DIR

def gen_excel_sheets(comp_id):
    comp_name = Company.query.filter_by(company_id=comp_id).with_entities(Company.name).first()[0]
    if comp_name is None:
        return
    filename = comp_name + ".xlsx"
    wb = Workbook()
    ws = wb.active
    ws.title = comp_name
    header = ['USN', 'Name', 'Email-ID', '10th %', '12th/Diploma %', 'CGPA']
    ws.append(header)
    usn = Registrations.query.filter_by(company_id=comp_id).with_entities(Registrations.usn).all()
    for u in usn:
        print(u)
        q = Student.query.get(str(u[0]))
        # stud_details = str(q).split(',')
        stud_details = [q.usn, q.name, q.email_id, q.tenth_percentage, q.twelfth_percentage, q.cgpa]
        ws.append(stud_details)
    wb.save(os.path.join(EXCEL_FILES_DIR, filename))
    return filename
