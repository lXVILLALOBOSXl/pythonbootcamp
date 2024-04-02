from flask import Flask
import random

random_number = random.randint(0, 9)
print(random_number)

app = Flask(__name__)

@app.route("/")
def index():
    return '<h1>Guess a number between 0 and 9</h1>' \
           '<img src="https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif" alt="Gif counting from 1 to 10">'

@app.route("/<int:number>")
def greetings(number):
    if number > random_number:
        return '<h1 style="color: purple;">To high, try again!</h1>' \
               '<img src="https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif" alt="Little dog">'
    elif number < random_number:
        return '<h1 style="color: red;">To low, try again!</h1>' \
               '<img src="https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif" alt="Little dog">'
    else:
        return '<h1 style="color: green;">You found me!</h1>' \
               '<img src="https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif" alt="Little dog">'

if __name__ == "__main__":
    app.run(debug=True)