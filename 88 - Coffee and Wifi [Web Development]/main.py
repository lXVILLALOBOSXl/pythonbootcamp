from flask import Flask, render_template, redirect, url_for, request, send_from_directory
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin, login_user, LoginManager, current_user, logout_user, login_required
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Float, Date
from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, FloatField, SubmitField, DateField, PasswordField, BooleanField
from wtforms.validators import DataRequired
from urllib.parse import urlencode
import requests

CAFE_DB_API_KEY = "TopSecretAPIKey"
CAFE_DB_API = "http://127.0.0.1:5000"

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap5(app)

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


class LoginAdminForm(FlaskForm):
    username = StringField(label='Username', validators=[DataRequired()])
    password = PasswordField(label='Password', validators=[DataRequired()])
    submit = SubmitField(label='Login')

class AddCafeForm(FlaskForm):
    name = StringField(label='Name', validators=[DataRequired()])
    map_url = StringField(label='Map URL', validators=[DataRequired()])
    img_url = StringField(label='Image URL', validators=[DataRequired()])
    location = StringField(label='Location', validators=[DataRequired()])
    has_sockets = BooleanField(label='Has Sockets')
    has_toilet = BooleanField(label='Has Toilet')
    has_wifi = BooleanField(label='Has Wifi')
    can_take_calls = BooleanField(label='Can Take Calls')
    seats = StringField(label='Seats', validators=[DataRequired()])
    coffee_price = StringField(label='Coffee Price', validators=[DataRequired()])
    submit = SubmitField(label='Add Cafe')


@app.route("/")
def home():
    response = requests.get(f"{CAFE_DB_API}/all")
    all_cafes = response.json()
    all_cafes = all_cafes['cafes']
    return render_template("index.html", cafes=all_cafes)

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
    response = requests.get(f"{CAFE_DB_API}/all")
    all_cafes = response.json()
    all_cafes = all_cafes['cafes']
    return render_template("admin.html", cafes=all_cafes)

@app.route("/add", methods=["GET", "POST"])
def add():
    form = AddCafeForm()
    if form.validate_on_submit():

        payload = {
            "name": form.name.data,
            "map_url": form.map_url.data,
            "img_url": form.img_url.data,
            "loc": form.location.data,
            "seats": form.seats.data,
            "toilet": "true" if form.has_toilet.data else "false",
            "wifi": "true" if form.has_wifi.data else "false",
            "sockets": "true" if form.has_sockets.data else "false",
            "calls": "true" if form.can_take_calls.data else "false",
            "coffee_price": form.coffee_price.data
        }

        encoded_payload = urlencode(payload)
        url = f"{CAFE_DB_API}/add?api-key={CAFE_DB_API_KEY}"
        headers = {"Content-Type": "application/x-www-form-urlencoded"}

        response = requests.post(url, headers=headers, data=encoded_payload)


        return redirect(url_for('home'))
    return render_template("add.html", form=form)

@app.route("/edit", methods=["GET", "POST"])
@login_required
def edit():
    cafe_id = request.args.get('id')
    cafe = requests.get(f"{CAFE_DB_API}/cafe/{cafe_id}").json()
    cafe = cafe['cafe']
    form = AddCafeForm(
        name=cafe['name'],
        map_url=cafe['map_url'],
        img_url=cafe['img_url'],
        location=cafe['location'],
        seats=cafe['seats'],
        has_toilet=True if cafe['has_toilet'] == 'true' else False,
        has_wifi=True if cafe['has_wifi'] == 'true' else False,
        has_sockets=True if cafe['has_sockets'] == 'true' else False,
        can_take_calls=True if cafe['can_take_calls'] == 'true' else False,
        coffee_price=cafe['coffee_price']
    )
    if form.validate_on_submit():
        payload = {
            "name": form.name.data,
            "map_url": form.map_url.data,
            "img_url": form.img_url.data,
            "location": form.location.data,
            "seats": form.seats.data,
            "has_toilet": "true" if form.has_toilet.data else "false",
            "has_wifi": "true" if form.has_wifi.data else "false",
            "has_sockets": "true" if form.has_sockets.data else "false",
            "can_take_calls": "true" if form.can_take_calls.data else "false",
            "coffee_price": form.coffee_price.data
        }

        encoded_payload = urlencode(payload)
        url = f"{CAFE_DB_API}/edit/{cafe_id}?api-key={CAFE_DB_API_KEY}"
        headers = {"Content-Type": "application/x-www-form-urlencoded"}

        response = requests.patch(url, headers=headers, data=encoded_payload)

        return redirect(url_for('admin'))
    return render_template("edit.html", form=form, cafe=cafe)

@app.route("/delete", methods=["GET", "POST"])
@login_required
def delete():
    cafe_id = request.args.get('id')
    url = f"{CAFE_DB_API}/report-closed/{cafe_id}?api-key={CAFE_DB_API_KEY}"
    response = requests.delete(url)
    return redirect(url_for('admin'))

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True, port=5001)

