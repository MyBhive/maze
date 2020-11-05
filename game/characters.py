# coding: utf-8

"""Create a class Character
with attribute the character, and his x,y position
"""


class Character:
    def __init__(self, character, pos_x, pos_y):
        self.character = character
        self.pos_x = int(pos_x)
        self.pos_y = int(pos_y)

    def picture_from_character(self, character):
        self.character = character
        return self.character


""" Create the McGyver class out of the mother class: Character
using 'M' for McGyver
McGyver also owns a inventory to collect items in the game.
"""


class McGyver(Character):
    def __init__(self, pos_x, pos_y):
        super().__init__("M", pos_x, pos_y)
        self.inventory = []
        self.pos_x = pos_x
        self.pos_y = pos_y

    """ Method to move Mc Gyver in the maze depending on the player orders.
    Up / Down : the y position change 
    Left / Right : the x position change
    """

    def move_mcgyver(self, direction):
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

    """ To collect items and add them in the inventory """

    def collect_item(self, item):
        self.inventory.append(item)


""" Create the Guardian class out of the mother class: Character
Using "G" for Guardian
"""


class Guardian(Character):
    def __init__(self, pos_x, pos_y,):
        super().__init__("G", pos_x, pos_y)

    def position(self):
        return self.pos_x, self.pos_y
