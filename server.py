from flask import Flask
import random

random_value = random.randint(0, 10)

app = Flask(__name__)


@app.route('/')
def home():
    return '<h1>Guess a number between 0 and 9</h1>' \
           '<img src="https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif" />'


@app.route('/<int:number>')
def guess_number(number):
    if number < random_value:
        return '<h1 style="color: grey;">Too low, try again!</h1>' \
               '<img src="https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif" />'
    elif number > random_value:
        return '<h1 style="color: red;">Too high, try again!</h1>' \
               '<img src="https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif" />'
    else:
        return '<h1 style="color: green;">You found me!</h1>' \
               '<img src="https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif" />'


if __name__ == '__main__':
    app.run(debug=True)
