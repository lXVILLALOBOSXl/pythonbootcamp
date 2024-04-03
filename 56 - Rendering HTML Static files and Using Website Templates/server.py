from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/birthday")
def birthday():
    return render_template('birthday.html')

@app.route("/cv")
def cv():
    return render_template('cv.html')

if __name__ == "__main__":
    app.run(debug=True)