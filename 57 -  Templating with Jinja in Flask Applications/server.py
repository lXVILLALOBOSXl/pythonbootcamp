from flask import Flask, render_template
import requests
from datetime import datetime
import random

app = Flask(__name__)

def api_request(name):
    response = requests.get(f"https://api.agify.io?name={name}")
    response.raise_for_status()
    age = response.json()["age"]

    response = requests.get(f"https://api.genderize.io?name={name}")
    response.raise_for_status()
    gender = response.json()["gender"]

    return age, gender

@app.route("/")
def home():
    random_number = random.randint(1,10)
    current_year = datetime.now().year
    company = 'Monsters incorporated'
    return render_template('index.html', num=random_number, year=current_year, company=company)

@app.route("/guess/<name>")
def guess(name):
    result = api_request(name)
    age = result[0]
    gender = result[1]
    name = name[0].upper() + name[1:]

    return render_template('guess.html', name=name, gender=gender, age=age)

@app.route("/blog/<num>")
def get_blog(num):
    print(num)
    response = requests.get(f"https://api.npoint.io/c790b4d5cab58020d391")
    response.raise_for_status()
    result = response.json()

    return render_template('blog.html', posts=result)

if __name__ == "__main__":
    app.run(debug=True)