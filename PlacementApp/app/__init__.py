from flask import Flask, render_template
app = Flask(__name__)

import app.views

@app.errorhandler(404)
def not_found(error):
    return render_template('404.html'), 404
