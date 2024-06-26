from datetime import date
from flask import Flask, abort, render_template, redirect, url_for, flash, request
from flask_bootstrap import Bootstrap5
from flask_ckeditor import CKEditor
from flask_login import UserMixin, login_user, LoginManager, current_user, logout_user
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import relationship, DeclarativeBase
from sqlalchemy import Integer, String, Text, Enum, Column, ForeignKey, Date
from functools import wraps
from werkzeug.security import generate_password_hash, check_password_hash
from forms import CreateTaskForm, RegisterForm, LoginForm 


app = Flask(__name__)
app.config['SECRET_KEY'] = ''
ckeditor = CKEditor(app)
Bootstrap5(app)

login_manager = LoginManager()
login_manager.init_app(app)

@login_manager.user_loader
def load_user(user_id):
    return db.get_or_404(User, user_id)


# CREATE DATABASE
class Base(DeclarativeBase):
    pass
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///todo.db'
db = SQLAlchemy(model_class=Base)
db.init_app(app)


# CONFIGURE TABLES
class User(UserMixin, db.Model):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String(50), unique=True, nullable=False)
    password = Column(String(255), nullable=False)
    email = Column(String(100), unique=True, nullable=False)
    tasks = relationship('Task', back_populates='user', cascade='all, delete, delete-orphan')

class Task(db.Model):
    __tablename__ = 'tasks'
    task_id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey('users.id', ondelete='CASCADE'), nullable=False)
    title = Column(String(255), nullable=False)
    description = Column(Text)
    status = Column(Enum('pending', 'in_progress', 'completed', name='status_enum'), default='pending')
    due_date = Column(Date, nullable=False)
    user = relationship('User', back_populates='tasks')


with app.app_context():
    db.create_all()

@app.route('/register', methods=["GET", "POST"])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        email = form.email.data
        result = db.session.execute(db.select(User).where(User.email == email))
        user = result.scalar()
        if user:
            flash("You've already signed up with that email, log in instead!")
            return redirect(url_for('login'))
        hash_and_salted_password = generate_password_hash(
            form.password.data,
            method='pbkdf2:sha256',
            salt_length=8
        )
        new_user = User(
            email=form.email.data,
            password=hash_and_salted_password,
            username=form.username.data,
        )
        db.session.add(new_user)
        db.session.commit()
        login_user(new_user)
        return redirect(url_for("get_all_tasks"))
    # Passing True or False if the user is authenticated. 
    return render_template("register.html", logged_in=current_user.is_authenticated, form=form)


# TODO: Retrieve a user from the database based on their email. 
@app.route('/login', methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        email = form.email.data
        password = form.password.data
        result = db.session.execute(db.select(User).where(User.email == email))
        user = result.scalar()
        if not user:
            flash("That email does not exist, please try again.")
            return redirect(url_for('login'))
        elif not check_password_hash(user.password, password):
            flash('Password incorrect, please try again.')
            return redirect(url_for('login'))
        else:
            login_user(user)
            return redirect(url_for('get_all_tasks'))
    return render_template("login.html", logged_in=current_user.is_authenticated, form=form)


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('get_all_tasks'))


@app.route('/')
def get_all_tasks():
    user = current_user
    if not user.is_authenticated:
        return redirect(url_for('login'))
    # Get the tasks from the current user
    result = db.session.execute(db.select(Task).where(Task.user_id == user.id))
    tasks = result.scalars().all()
    return render_template("index.html", all_tasks=tasks, logged_in=current_user.is_authenticated, current_user=current_user)


@app.route("/new-task", methods=["GET", "POST"])
def add_new_task():
    form = CreateTaskForm()
    if form.validate_on_submit():
        new_task = Task(
            title=form.title.data,
            description=form.description.data,
            due_date=form.due_date.data,
            user=current_user,
            status='pending'
        )
        db.session.add(new_task)
        db.session.commit()
        return redirect(url_for("get_all_tasks"))
    return render_template("make-task.html", form=form, logged_in=current_user.is_authenticated, current_user=current_user)

@app.route("/start-task/<int:task_id>")
def start_task(task_id):
    task = db.get_or_404(Task, task_id)
    if task.user_id != current_user.id:
        abort(403)
    task.status = 'in_progress'
    db.session.commit()
    return redirect(url_for('get_all_tasks'))

@app.route("/complete-task/<int:task_id>")
def complete_task(task_id):
    task = db.get_or_404(Task, task_id)
    if task.user_id != current_user.id:
        abort(403)
    task.status = 'completed'
    db.session.commit()
    return redirect(url_for('get_all_tasks'))

@app.route("/cancel-task/<int:task_id>")
def cancel_task(task_id):
    task = db.get_or_404(Task, task_id)
    if task.user_id != current_user.id:
        abort(403)
    task.status = 'pending'
    db.session.commit()
    return redirect(url_for('get_all_tasks'))

@app.route("/undo-task/<int:task_id>")
def undo_task(task_id):
    task = db.get_or_404(Task, task_id)
    if task.user_id != current_user.id:
        abort(403)
    task.status = 'in_progress'
    db.session.commit()
    return redirect(url_for('get_all_tasks'))

@app.route("/edit-task/<int:task_id>")
def edit_task(task_id):
    task = db.get_or_404(Task, task_id)
    if task.user_id != current_user.id:
        abort(403)
    form = CreateTaskForm(
        title=task.title,
        description=task.description,
        due_date=task.due_date
    )
    if form.validate_on_submit():
        task.title = form.title.data
        task.description = form.description.data
        task.due_date = form.due_date.data
        db.session.commit()
        return redirect(url_for('get_all_tasks'))
    return render_template("make-task.html", form=form, logged_in=current_user.is_authenticated, current_user=current_user)

@app.route("/delete-task/<int:task_id>")
def delete_task(task_id):
    task = db.get_or_404(Task, task_id)
    if task.user_id != current_user.id:
        abort(403)
    db.session.delete(task)
    db.session.commit()
    return redirect(url_for('get_all_tasks'))


if __name__ == "__main__":
    app.run(debug=True)
