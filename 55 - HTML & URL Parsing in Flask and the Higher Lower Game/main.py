from flask import Flask

app = Flask(__name__)

def make_underlined(function):
    def underline():
        return f'<u>{function()}</u>'
    return underline

def make_emphasis(function):
    def emphasis():
        return f'<em>{function()}</em>'
    return emphasis

def make_bold(function):
    def bold():
        return f'<b>{function()}</b>'
    return bold

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/bye")
@make_underlined
@make_emphasis
@make_bold
def bye():
    return "<p>Bye2</p>"

@app.route("/greeting/<name>/<int:age>")
def greetings(name, age):
    return f"<p>Hi {name}, and you are {age} years old</p>"

if __name__ == "__main__":
    app.run(debug=True)