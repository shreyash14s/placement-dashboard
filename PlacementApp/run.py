# Run a test server.
from app import fapp
import config

fapp.run(host='0.0.0.0', port=8080, debug=config.DEBUG)

# To initiate database
# import app.database
# app.database.init_db()
