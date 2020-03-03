from flask import Flask

# The WSGI configuration on Elastic Beanstalk requires
# the callable be named 'application' by default.
application = Flask(__name__)

# Import the views
from app.views import main