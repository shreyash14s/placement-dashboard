# Run a test server.
from app import app
import config

app.run(host='0.0.0.0', port=8080, debug=config.DEBUG)
