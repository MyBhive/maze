
"""
Creating a Items class to give a name and a position to all the items of the game.
"""


class Items:

    def __init__(self, name, x, y):
        self.name = name
        self.x = int(x)
        self.y = int(y)

    def get_position(self, x, y):
        return x, y

    def collected(self):
       return True

    def has_all_items(self):
        if Items.collected(self.name) == 3:
            return True
        else:
            return False


