from flask import render_template, Blueprint
from flask_login import login_required

account = Blueprint('account', __name__, template_folder='templates')


@account.route('/account/')
@account.route('/account/<name>')
@login_required
def account(name):
    return render_template('account.html')
