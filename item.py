"""
Creating an Items class to give a name and a position x,y to all the items of the game.
"""


class Items:

    def __init__(self, name, x, y):
        self.name = name
        self.x = int(x)
        self.y = int(y)
        self.is_collected = False

    """
    To set the x,y position of the item in the maze
    """
    def set_position(self):
        return self.x, self.y

    """
    Through this booleen method, the item can be collected an added to the hero's inventory
    """
    def go_to_inventory(self):
        self.is_collected = True
