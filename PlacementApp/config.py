# Statement for enabling the development environment
DEBUG = True

# Define the application directory
import os
BASE_DIR = os.path.abspath(os.path.dirname(__file__))
EXCEL_FILES_DIR = os.path.join(BASE_DIR, 'excels')
os.makedirs(EXCEL_FILES_DIR, exist_ok=True)

# Define the database - we are working with
# SQLite for this example
# SQLALCHEMY_DATABASE_URI = 'mysql+pymysql:///' + os.path.join(BASE_DIR, 'app.db')
# SQLALCHEMY_DATABASE_URI = 'mysql+pymysql:////Users/sarnayak/Desktop/app.db'
# SQLALCHEMY_DATABASE_URI = 'mysql+pymysql:///file.db'
SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:shreyash@localhost/placement'
# /Users/sarnayak/Desktop/Sem7/SE_Project/placement-dashboard/PlacementApp/
DATABASE_CONNECT_OPTIONS = {}

# Application threads. A common general assumption is
# using 2 per available processor cores - to handle
# incoming requests using one and performing background
# operations using the other.
THREADS_PER_PAGE = 2

# Enable protection agains *Cross-site Request Forgery (CSRF)*
CSRF_ENABLED = True

# Use a secure, unique and absolutely secret key for
# signing the data. 
CSRF_SESSION_KEY = "secret"

# Secret key for signing cookies
SECRET_KEY = "secret"
