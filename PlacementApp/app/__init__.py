from flask import Flask, render_template
from config import SECRET_KEY
fapp = Flask(__name__,
            static_url_path='', 
            static_folder='static')
fapp.config['SESSION_TYPE'] = 'memcached'
fapp.config['SECRET_KEY'] = SECRET_KEY

import app.views
from app.models import Student, Company

@fapp.errorhandler(404)
def not_found(error):
    return render_template('404.html'), 404
