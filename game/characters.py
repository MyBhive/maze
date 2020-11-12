# coding: utf-8

"""Create a mother class Character
and the children classes Mcgyver and Guardien"""


class Character:
    """Create a class Character
    with attribute the character, and his x,y position"""
    def __init__(self, character, pos_x, pos_y):
        """Initialize the character and his position"""
        self.character = character
        self.pos_x = int(pos_x)
        self.pos_y = int(pos_y)


class McGyver(Character):
    """Create the McGyver class out of the mother class: Character
    using 'M' for McGyver
    McGyver also owns a inventory to collect items in the game."""
    def __init__(self, pos_x, pos_y):
        """Initialize McGyver position
        and his inventory as an empty list"""
        super().__init__("M", pos_x, pos_y)
        self.inventory = []
        self.pos_x = pos_x
        self.pos_y = pos_y

    def move_mcgyver(self, direction):
        """Method to move Mc Gyver in the maze
        depending on the player orders.
        Up / Down : the y position change
        Left / Right : the x position change"""
        if direction == "u":
            self.pos_y -= 1
        elif direction == "d":
            self.pos_y += 1
        if direction == "l":
            self.pos_x -= 1
        elif direction == "r":
            self.pos_x += 1
        else:
            return False

    def collect_item(self, item):
        """To collect items and add them in the inventory"""
        self.inventory.append(item)


class Guardian(Character):
    """Create the Guardian class out of the mother class: Character
    Using "G" for Guardian"""
    def __init__(self, pos_x, pos_y,):
        """Initialize the guardian position"""
        super().__init__("G", pos_x, pos_y)

    def position(self):
        """Method to know the guardian position"""
        return self.pos_x, self.pos_y
