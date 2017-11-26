from openpyxl import Workbook
from app.models import Company, Registrations, Student

def gen_excel_sheets(comp_id):
    comp_name = Company.query.filter_by(company_id=comp_id).with_entities(Company.name).first()
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
        q = Student.query.get(str(u[0]))
        stud_details = str(q).split(',')
        ws.append(stud_details)
    wb.save(filename)
    return filename
