from flask import Flask, render_template
fapp = Flask(__name__)

import app.views

@fapp.errorhandler(404)
def not_found(error):
    return render_template('404.html'), 404
