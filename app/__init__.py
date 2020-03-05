from flask import Flask
from flask_login import LogInManager

# The WSGI configuration on Elastic Beanstalk requires
# the callable be named 'application' by default.
app = Flask(__name__)

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "login"

@login_manager.user_loader
def load_user(user_id):
    return User.get(user_id)

# Import the views
from app.views import main
