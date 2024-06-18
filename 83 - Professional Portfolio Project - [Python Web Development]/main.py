from flask import Flask, render_template, redirect, url_for, request, send_from_directory
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin, login_user, LoginManager, current_user, logout_user, login_required
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Float, Date
from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, FloatField, SubmitField, DateField, PasswordField
from wtforms.validators import DataRequired

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap5(app)

# @app.route('/node_modules/<path:filename>')
# def node_modules(filename):
#     return send_from_directory('node_modules', filename)

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

class User(UserMixin):
    def __init__(self, id):
        self.id = id   

@login_manager.user_loader
def load_user(user_id):
    if user_id == '1':
        return User(user_id)
    return None

##CREATE DB
class Base(DeclarativeBase):
    pass
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///portfolio.db'
db = SQLAlchemy(model_class=Base)
db.init_app(app)


##CREATE TABLE
class Project(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), nullable=False)
    description = db.Column(db.String(250), nullable=False)
    date = db.Column(Date, nullable=False)
    github = db.Column(db.String(250), nullable=False)
    link = db.Column(db.String(250), nullable=True)
    img_url = db.Column(db.String(250), nullable=True)

with app.app_context():
    db.create_all()

class LoginAdminForm(FlaskForm):
    username = StringField(label='Username', validators=[DataRequired()])
    password = PasswordField(label='Password', validators=[DataRequired()])
    submit = SubmitField(label='Login')

class ContactForm(FlaskForm):
    name = StringField(label='Name', validators=[DataRequired()])
    email = StringField(label='Email', validators=[DataRequired()])
    message = StringField(label='Message', validators=[DataRequired()])
    submit = SubmitField(label='Send')

class AddProjectForm(FlaskForm):
    title = StringField(label='Title', validators=[DataRequired()])
    description = StringField(label='Description', validators=[DataRequired()])
    date = DateField(label='Date', validators=[DataRequired()])
    github = StringField(label='Github', validators=[DataRequired()])
    link = StringField(label='Link')
    img_url = StringField(label='Image URL')
    submit = SubmitField(label='Save Project')


@app.route("/")
def home():
    result = db.session.execute(db.select(Project).order_by(Project.date.desc()))
    all_projects = result.scalars().all() # convert ScalarResult to Python List
    return render_template("index.html", projects=all_projects)

@app.route("/contact", methods=["GET", "POST"])
def contact():
    form = ContactForm()
    if form.validate_on_submit():
        return redirect(url_for('home'))
    return render_template("contact.html", form=form)


@app.route("/login", methods=["GET", "POST"])
def login():
    form = LoginAdminForm()
    if form.validate_on_submit():
        if form.username.data == "admin" and form.password.data == "admin":
            user = User(1)
            login_user(user)
            return redirect(url_for('admin'))
    return render_template("login.html", form=form)


@app.route("/admin")
@login_required
def admin():
    result = db.session.execute(db.select(Project).order_by(Project.date.desc()))
    all_projects = result.scalars().all()
    return render_template("admin.html", projects=all_projects)

@app.route("/add", methods=["GET", "POST"])
@login_required
def add():
    form = AddProjectForm()
    if form.validate_on_submit():
        new_project = Project(
            title=form.title.data,
            description=form.description.data,
            date=form.date.data,
            github=form.github.data,
            link=form.link.data,
            img_url=form.img_url.data
        )
        db.session.add(new_project)
        db.session.commit()
        return redirect(url_for('admin'))
    return render_template("add.html", form=form)

@app.route("/edit", methods=["GET", "POST"])
@login_required
def edit():
    project_id = request.args.get('id')
    project = db.get_or_404(Project, project_id)
    if project is None:
        return redirect(url_for('admin'))
    form = AddProjectForm(request.form, obj=project)
    if form.validate_on_submit():
        project.title = form.title.data
        project.description = form.description.data
        project.date = form.date.data
        project.github = form.github.data
        project.link = form.link.data
        project.img_url = form.img_url.data
        db.session.commit()
        return redirect(url_for('admin'))
    return render_template("edit.html", form=form, project=project)

@app.route("/delete", methods=["GET", "POST"])
@login_required
def delete():
    project_id = request.args.get('id')
    project = db.get_or_404(Project, project_id)
    if project is None:
        return redirect(url_for('admin'))
    db.session.delete(project)
    db.session.commit()
    return redirect(url_for('admin'))

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True)

