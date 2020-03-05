import flask
from flask import Blueprint, request, render_template, redirect
from flask_login import login_user, login_required, logout_user
from is_safe_url import is_safe_url
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField

loginHandler = Blueprint('loginHandler', __name__, template_folder='templates')


class LoginForm(FlaskForm):
    username = StringField('Username')
    password = PasswordField('Password')
    submit = SubmitField('Submit')


@loginHandler.route('/login', methods=['GET', 'POST'])
def login():
    # Here we use a class of some kind to represent and validate our
    # client-side form data. For example, WTForms is a library that will
    # handle this for us, and we use a custom LoginForm to validate.
    if request.method == 'POST':
        form = LoginForm()
        if form.validate_on_submit():
            # Login and validate the user.
            # user should be an instance of your `User` class
            login_user(user)

            flask.flash('Logged in successfully.')

            # TODO: Don't use the variable next here it shadows built in variable
            next = flask.request.args.get('next')
            # is_safe_url should check if the url is safe for redirects.
            # See http://flask.pocoo.org/snippets/62/ for an example.
            if not is_safe_url(next):
                return flask.abort(400)

            return flask.redirect(next or flask.url_for('account'))

    return render_template('login.html')


@loginHandler.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect("url_for('index')")
