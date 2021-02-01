from flask import Flask
from random import choice
# TODO: Follow the assignment instructions to complete the required routes!
# (And make sure to delete this TODO message when you're done!)

app = Flask(__name__)


@app.route('/')
def homepage():
    """Shows a greeting to the user """
    return 'Are you there, world? It\'s me, Ducky!'

# ---------------- Users Favorite Animal -------------------


@app.route('/animal/<users_animal>')
def favorite_animal(users_animal):
    """ Display a message to the user that changes based on their favorite animal. """
    return f"Wow, {users_animal} is my favorite animal, too!"

# ---------------- Users Favorite Dessert -------------------


@app.route('/dessert/<users_dessert>')
def favorite_dessert(users_dessert):
    return f"How did you know I liked {users_dessert}?"

# ---------------- Madlibs ----------------------------------


@app.route('/madlibs/<adjective>/<noun>')
def madlibs(adjective, noun):
    return f"The {adjective} {noun} ran up a tree, to drink some tea."

# ---------------- Multiply 2 Numbers -------------------


@app.route('/multiply/<number1>/<number2>')
def multiply(number1, number2):
    if number1.isdigit() and number2.isdigit():
        total = int(number1) * int(number2)
        return f" The total is {total}"
    else:
        return f"Invalid inputs. Please try again by entering 2 numbers!"

# ---------------- Say N Times -------------------
# Needs help!!!!!!


@app.route('/sayntimes/<word>/<n>')
def loop(word, n):
    completeWord = ""
    for i in range(int(n)):
        completeWord += word
    return completeWord

# ---------------- Dice Game -------------------


@app.route('/dicegame')
def diceGame():
    dice = [1, 2, 3, 4, 5, 6]
    roll = choice(dice)
    if roll == 6:
        return f"You rolled a {roll}. You won!"
    else:
        return f"You rolled a {roll}. You lost!"

    # ---------------- Testing -------------------

    # ----------------------- Bottom ------------------
if __name__ == '__main__':
    app.run(debug=True)
