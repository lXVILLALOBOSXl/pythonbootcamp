from flask import Flask, render_template
import requests

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
    return render_template('post.html', title=target_post['title'], body=target_post['body'])

if __name__ == "__main__":
    app.run(debug=True)
