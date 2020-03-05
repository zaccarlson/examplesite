from flask import render_template
from app import app



@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', title='Home')

@app.route('/account/')
@app.route('/account/<name>')
@login_required
def account():
    return render_template('account.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    # Here we use a class of some kind to represent and validate our
    # client-side form data. For example, WTForms is a library that will
    # handle this for us, and we use a custom LoginForm to validate.
    form = LoginForm()
    if form.validate_on_submit():
        # Login and validate the user.
        # user should be an instance of your `User` class
        login_user(user)

        flask.flash('Logged in successfully.')

        next = flask.request.args.get('next')
        # is_safe_url should check if the url is safe for redirects.
        # See http://flask.pocoo.org/snippets/62/ for an example.
        if not is_safe_url(next):
            return flask.abort(400)

        return flask.redirect(next or flask.url_for('account'))
    return flask.render_template('login.html', form=form)

@app.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect('url_for('index'))