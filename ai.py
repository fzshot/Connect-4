from random import randrange


class Human():
    """Keyboard Agent"""

    def play(self):
        position = raw_input("Enter the position for " + "X" + ": ")
        return position

class RandomAgent():
    """This strategy plays in an random column."""

    def play(self):
        position = randrange(1,7)
        print "Random Agent: inserted at", position
        return position
