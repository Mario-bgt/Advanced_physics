"""Implement a class Coinflips which can be used to play multiple rounds of flipping a coin and guessing which side it
 will land on. The player wins if an absolute majority of his guesses were correct.
Coinflips should implement a method play which takes the player's guess as a string parameter, either "heads" or "tails".
 A Warning should be raised if some other string is passed. play then randomly selects the result of the coin flip for
  the current round of the game. play should return a string "heads" or "tails" depending on the random result. A
  method winner can be called at any
time to determine, whether the player's guesses were correct a majority of the time. winner should return True if the
 player wins, False otherwise. The player can continue playing for more rounds even after calling winner. Finally,
  the string representation of a Coinflips instance should be the history of "heads" and "tails" that occurred in
  the game.
Important: The examples contain essential information, such as how the methods should be called and used and what the
string representation of Coinflips should look like. Make sure your implementation works with the provided examples.
Use the following template:"""


import random

class Coinflips:
    def __init__(self):
        self.__log = []
        self.__lyst = []

    def __str__(self):
        return ", ".join(self.__lyst)

    def play(self, guess):
        if guess not in ["heads", "tails"]:
            raise Warning
        num = random.randint(1, 2)
        if num == 1:
            trow = "heads"
        else:
            trow = "tails"
        self.__lyst.append(trow)
        if guess == trow:
            self.__log.append(True)
        else:
            self.__log.append(False)
        return trow

    def winner(self):
        if len(self.__log)/2 > len([i for i in self.__log if i == True]):
            return True
        return False


t = Coinflips()
try:
    t.play("arms")
except Warning:
    print("invalid choice")
# Your play results may be different from this example due to randomness
print(t.play("heads"))
print(t.play("tails"))
print(t.play("heads"))
print(t)
print(t.winner())