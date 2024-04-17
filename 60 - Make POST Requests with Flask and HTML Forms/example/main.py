from flask import Flask, render_template, request
import requests

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/login', methods=["POST"])
def receive_data():
    return f"<h1>Name: {request.form['name']} Email: {request.form['email']} Password: {request.form['password']}</h1>"


if __name__ == "__main__":
    app.run(debug=True)
