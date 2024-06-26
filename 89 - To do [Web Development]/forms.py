from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, DateField
from wtforms.validators import DataRequired, URL, Email
from flask_ckeditor import CKEditorField


class CreateTaskForm(FlaskForm):
    title = StringField("Task Title", validators=[DataRequired()])
    description = CKEditorField("Task Description", validators=[DataRequired()])
    due_date = DateField("Due Date", validators=[DataRequired()])
    submit = SubmitField("Add Task")


class RegisterForm(FlaskForm):
    email = StringField("Email", validators=[DataRequired(), Email()])
    password = PasswordField("Password", validators=[DataRequired()])
    username = StringField("Username", validators=[DataRequired()])
    submit = SubmitField("Sign Me Up!") 


class LoginForm(FlaskForm):
    email = StringField("Email", validators=[DataRequired(), Email()])
    password = PasswordField("Password", validators=[DataRequired()])
    submit = SubmitField("Let Me In!")

