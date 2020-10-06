
"""
Creating a Items class to give a name and a position to all the items of the game.
"""


class Items:

    def __init__(self, name, x, y):
        self.name = name
        self.x = x
        self.y = y
        self.inventury = []

    def set_position(self, x, y):
        self.x = x
        self.y = y
