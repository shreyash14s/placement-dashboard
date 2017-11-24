from app import fapp

@fapp.route('/')
def index():
    return 'Hello World!'
