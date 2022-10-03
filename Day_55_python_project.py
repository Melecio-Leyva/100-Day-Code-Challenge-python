from flask import Flask
import random

random_number = random.randint(0, 9)
print(random_number)

app = Flask(__name__)

# App decorator home route
@app.route('/')
def home():
    return "<h1>Guess a number between 0 and 9</h1>" \
           "<img src='https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif'/>"


# guess a number in the header of the address
@app.route("/<int:guess>")
def guess_number(guess):
    # check if number is greater than random
    if guess > random_number:
        return "<h1 style='color: purple'>Too high, try again!</h1>" \
               "<img src='https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif'/>"
    #check if number is les than random
    elif guess < random_number:
        return "<h1 style='color: red'>Too low, try again!</h1>"\
               "<img src='https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif'/>"
    # else correct choice!
    else:
        return "<h1 style='color: green'>You found me!</h1>" \
               "<img src='https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif'/>"

# turn debugger on.
if __name__ == "__main__":
    app.run(debug=True)
