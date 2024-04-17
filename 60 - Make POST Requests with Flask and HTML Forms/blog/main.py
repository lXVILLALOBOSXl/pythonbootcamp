from flask import Flask, render_template, request
import requests
from notification_manager import NotificationManager 

app = Flask(__name__)

@app.route('/')
def home():
    response = requests.get(f"https://api.npoint.io/c790b4d5cab58020d391")
    response.raise_for_status()
    result = response.json()
    return render_template("index.html", posts=result)

@app.route("/post/<id>")
def get_post(id):
    id = int(id)
    response = requests.get(f"https://api.npoint.io/c790b4d5cab58020d391")
    response.raise_for_status()
    result = response.json()
    target_post = next((item for item in result if item["id"] == id), None)
    id2 = id
    return render_template('blog-details.html', title=target_post['title'], body=target_post['body'], id=id2)

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/contact', methods=["POST"])
def send_info():
    name = request.form['name']
    email = request.form['email']
    subject = request.form['subject']
    message = request.form['message']
    nm = NotificationManager()
    nm.send_email('oslovdobrov@gmail.com',f"{name}: {subject}",f"{message}/n/nFrom:{email}")
    return render_template('contact.html')

if __name__ == "__main__":
    app.run(debug=True)
