from flask import Flask, render_template
fapp = Flask(__name__)

import app.views
from app.models import Student, Company

@fapp.errorhandler(404)
def not_found(error):
    return render_template('404.html'), 404
