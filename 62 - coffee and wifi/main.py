from flask import Flask, render_template, redirect, url_for
from flask_bootstrap import Bootstrap5
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import DataRequired
import csv

'''
Red underlines? Install the required packages first: 
Open the Terminal in PyCharm (bottom left). 

On Windows type:
python -m pip install -r requirements.txt

On MacOS type:
pip3 install -r requirements.txt

This will install the packages from requirements.txt for this project.
'''

app = Flask(__name__)
app.config['SECRET_KEY'] = ''
Bootstrap5(app)


class CafeForm(FlaskForm):
    cafe_name = StringField(validators=[DataRequired()], label='Cafe Name')
    location = StringField(validators=[DataRequired()], label='Location')
    open = StringField(validators=[DataRequired()], label='Open')
    close = StringField(validators=[DataRequired()], label='Close')
    coffee = SelectField(
        label='Coffee',
        choices=[
            ('1', '☕'),
            ('2', '☕☕'),
            ('3', '☕☕☕'),
            ('4', '☕☕☕☕'),
            ('5', '☕☕☕☕☕')
        ],
        validators=[DataRequired()]
    )
    wifi = SelectField(
        label='Wifi',
        choices=[
            ('1', '💪'),
            ('2', '💪💪'),
            ('3', '💪💪💪'),
            ('4', '💪💪💪💪'),
            ('5', '💪💪💪💪💪')
        ],
        validators=[DataRequired()]
    )
    power = SelectField(
        label='Power',
        choices=[
            ('1', '🔌'),
            ('2', '🔌🔌'),
            ('3', '🔌🔌🔌'),
            ('4', '🔌🔌🔌🔌'),
            ('5', '🔌🔌🔌🔌🔌')
        ],
        validators=[DataRequired()]
    )
    submit = SubmitField(label="Add")

# Exercise:z
# add: Location URL, open time, closing time, coffee rating, wifi rating, power outlet rating fields
# make coffee/wifi/power a select element with choice of 0 to 5.
#e.g. You could use emojis ☕️/💪/✘/🔌
# make all fields required except submit
# use a validator to check that the URL field has a URL entered.
# ---------------------------------------------------------------------------


# all Flask routes below
@app.route("/")
def home():
    return render_template("index.html")


@app.route('/add', methods=['GET', 'POST'])
def add_cafe():
    form = CafeForm()
    if form.validate_on_submit():
        new_data = [
            form.cafe_name.data,
            form.location.data,
            form.open.data,
            form.close.data,
            form.coffee.data,
            form.wifi.data,
            form.power.data
        ]
        with open('cafe-data.csv', mode='a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(new_data)
        return redirect(url_for('home'))  # Redirect to the home page or a confirmation page
    # Exercise:
    # Make the form write a new row into cafe-data.csv
    # with   if form.validate_on_submit()
    return render_template('add.html', form=form)


@app.route('/cafes')
def cafes():
    with open('cafe-data.csv', newline='', encoding='utf-8') as csv_file:
        csv_data = csv.reader(csv_file, delimiter=',')
        list_of_rows = []
        for row in csv_data:
            list_of_rows.append(row)
            print(row[1])
    return render_template('cafes.html', cafes=list_of_rows)


if __name__ == '__main__':
    app.run(debug=True)
