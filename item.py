"""
Creating an Items class to give a name and a position to all the items of the game.
"""


class Items:

    def __init__(self, name, x, y):
        self.name = name
        self.x = int(x)
        self.y = int(y)
        self.is_collected = False

    def set_position(self):
        return self.x, self.y

    def go_to_inventory(self):
        self.is_collected = True

