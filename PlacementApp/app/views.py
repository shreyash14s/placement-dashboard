from app import fapp
from app.query import gen_excel_sheets
from flask import send_from_directory
from config import EXCEL_FILES_DIR

@fapp.route('/')
def index():
    return 'Hello World!'

@fapp.route("/generate/<comp_id>", methods=['GET'])
def get_excel(comp_id):
    filename = gen_excel_sheets(comp_id)
    if filename:
        return send_from_directory(EXCEL_FILES_DIR, filename, as_attachment=True)
