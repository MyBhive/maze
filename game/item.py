# coding: utf-8

"""Creating an Items class
to give a name and a position x,y
to all the items of the game."""


class Items:

    def __init__(self, name, y, x):
        """Initialize the name and the position of each items"""
        super().__init__()
        self.name = name
        self.x = int(x)
        self.y = int(y)
        self.is_collected = False

    def go_to_inventory(self):
        """Through this booleen method,
        the item can be collected an added to the hero's inventory"""
        self.is_collected = True
