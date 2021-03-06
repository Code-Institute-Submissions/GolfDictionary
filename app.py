import os
from flask import Flask, render_template, redirect, request, url_for, flash
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from werkzeug.urls import url_parse
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import current_user, login_user, logout_user, login_required, LoginManager, UserMixin
from flask_wtf import Form, FlaskForm
from wtforms import StringField, PasswordField
from wtforms.validators import DataRequired, Email, EqualTo


from os import path
if path.exists("env.py"):
    import env


class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    password2 = PasswordField(
        'Repeat Password', validators=[DataRequired(), EqualTo('password')])


app = Flask(__name__)

lm = LoginManager()
lm.init_app(app)
lm.login_view = 'login'

app.config['SECRET_KEY'] = "Your_secret_string"


MONGODB_URI = os.environ.get("MONGO_URIL")
app.config["MONGO_DBNAME"] = 'golfDictionary'
app.config["MONGO_URI"] = MONGODB_URI

mongo = PyMongo(app)


class LoginForm(Form):
    """Login form to access writing and settings pages"""
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])


class User(UserMixin):
    def __init__(self, username):
        self.username = username

    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        return self.username

    @staticmethod
    def validate_login(password_hash, password):
        return check_password_hash(password_hash, password)


@lm.user_loader
def load_user(username):
    u = mongo.db.users.find_one({"username": username})
    if not u:
        return None
    return User(u['username'])


@app.route('/')
def home():
    return render_template("homepage.html")


@app.route('/definitions')
def definitions_list():
    return render_template("definitions.html", title='Definitions', definitions=mongo.db.entries.find())


@app.route('/definitions/<def_id>')
def definition(def_id):
    the_def = mongo.db.entries.find_one({"_id": ObjectId(def_id)})
    return render_template("def.html", definition=the_def)


@app.route('/add_definition')
@login_required
def add_definition():
    return render_template('adddefinition.html',
        title='Add Definition', defi={})


@app.route('/insert_def', methods=['POST'])
def insert_def():
    entries = mongo.db.entries
    entries.insert_one(request.form.to_dict())
    return redirect(url_for('definitions_list'))


@app.route('/update_def/<def_id>', methods=['POST'])
def update_def(def_id):
    defs = mongo.db.entries
    defs.update({'_id': ObjectId(def_id)},
    {
        'name': request.form.get('name'),
        'definition': request.form.get('definition'),
        'picture': request.form.get('picture'),
        'pronunciation': request.form.get('pronunciation'),
        'type': request.form.get('type')
    })
    return redirect(url_for('definitions_list'))


@app.route('/delete_def/<def_id>')
@login_required
def delete_def(def_id):
    mongo.db.entries.remove({'_id': ObjectId(def_id)})
    return redirect(url_for('definitions_list'))


@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = LoginForm()
    if form.validate_on_submit():
        user = mongo.db.users.find_one({"username": form.username.data})
        if user and User.validate_login(user['password'], form.password.data):
            user_obj = User(username=user['username'])
            login_user(user_obj)
            flash("Logged in successfully")
            return redirect(url_for("home"))
        else:
            flash('Invalid username or password')
    return render_template('login.html', title='Sign In', form=form)


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('login'))


@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        users = mongo.db.users
        existing_user = users.find_one({'username': request.form['username']})
        if existing_user is None:
            formData = request.form.to_dict()
            _user = {
                'username': formData["username"],
                'email': formData["email"],
                'password': generate_password_hash(formData["password"]),
            }
            users.insert_one(_user)
            flash('Congratulations, you are now a registered user!')
            return redirect(url_for('login'))
        else:
            flash('Username already in use')
    return render_template('register.html', title='Register', form=form)


@app.route('/edit_def/<def_id>')
@login_required
def edit_def(def_id):
    the_def = mongo.db.entries.find_one({"_id": ObjectId(def_id)})
    return render_template('editdef.html', defi=the_def, title='Edit')


if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
        port=int(os.environ.get('PORT')))