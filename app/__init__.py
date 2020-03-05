from flask import Flask, render_template
from flask_login import LoginManager
from app.views.loginHandler import loginHandler
from app.views.account import account

app = Flask(__name__)

app.register_blueprint(loginHandler)
# app.register_blueprint(account)

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "loginHandler.login"


@login_manager.user_loader
def load_user(user_id):
    return User.get(user_id)


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', title='Home')


if __name__ == '__main__':
    app.run()
