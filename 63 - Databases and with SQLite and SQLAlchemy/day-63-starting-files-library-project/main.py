from flask import Flask, render_template, request, redirect, url_for
from flask_bootstrap import Bootstrap5
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import DataRequired
from dbconnection import read_records, create_record, delete_record, update_record
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
app.config['SECRET_KEY'] = 'a'
Bootstrap5(app)


class BookForm(FlaskForm):
    book_name = StringField(validators=[DataRequired()], label='Book Name')
    book_author = StringField(validators=[DataRequired()], label='Book Author')
    rating = SelectField(
        label='Rating',
        choices=[
            ('1','⭐'),
            ('2','⭐⭐'),
            ('3','⭐⭐⭐'),
            ('4','⭐⭐⭐⭐'),
            ('5','⭐⭐⭐⭐⭐')
        ],
        validators=[DataRequired()]
    )
    submit = SubmitField(label="Add")

class EditForm(FlaskForm):
    rating = SelectField(
        label='Rating',
        choices=[
            ('1','⭐'),
            ('2','⭐⭐'),
            ('3','⭐⭐⭐'),
            ('4','⭐⭐⭐⭐'),
            ('5','⭐⭐⭐⭐⭐')
        ],
        validators=[DataRequired()]
    )
    submit = SubmitField(label="Change Rating")

def convert_rating_to_stars(rating):
    return {
        '1': '⭐',
        '2': '⭐⭐',
        '3': '⭐⭐⭐',
        '4': '⭐⭐⭐⭐',
        '5': '⭐⭐⭐⭐⭐'
    }.get(rating, '')


@app.route('/')
def home():
    # READ METHOD
    all_books = read_records()
    return render_template("index.html", books=all_books)


@app.route("/add", methods=['GET', 'POST'])
def add():
    book_form = BookForm()
    if book_form.validate_on_submit():
        # ADD METHOD
        create_record(book_form.book_name.data,book_form.book_author.data,convert_rating_to_stars(book_form.rating.data))
        return redirect(url_for('home'))
    return render_template("add.html", form=book_form)

@app.route("/edit/<name>/<rating>", methods=['GET', 'POST'])
def edit(name, rating):
    edit_form = EditForm()
    if edit_form.validate_on_submit():
        # EDIT METHOD
        print(edit_form.rating.data)
        update_record(name=name, rating= convert_rating_to_stars(edit_form.rating.data))
        return redirect(url_for('home'))
    return render_template("edit.html", form=edit_form, name=name, rating=rating)

@app.route("/delete/<name>", methods=['GET', 'POST'])
def delete(name):
    # DELETE METHOD
    delete_record(name)
    return redirect(url_for('home'))


if __name__ == "__main__":
    app.run(debug=True)

