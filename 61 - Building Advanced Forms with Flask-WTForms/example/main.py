from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email
from flask_bootstrap import Bootstrap5 # pip install bootstrap-flask



class LoginForm(FlaskForm):
    email = StringField(validators=[DataRequired(),Email()], label='Email')
    password = PasswordField(validators=[DataRequired()], label='Password')
    submit = SubmitField(label="Log In")

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key' 
bootstrap = Bootstrap5(app) # initialise bootstrap-flask 

@app.route("/")
def home():
    return render_template('index.html')

@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@email.com' and form.password.data == '12345678':
            return render_template('success.html')
        else:
            return render_template('denied.html')
    return render_template('login.html', form=form)

if __name__ == '__main__':
    app.run(debug=True)

