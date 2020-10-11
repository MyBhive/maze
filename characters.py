
"""
Create a class Character with attribute
a position: pos_x for index of line
and pos_y for index of column
"""


class Character:
    def __init__(self, character, pos_x, pos_y):
        self.character = character
        self.pos_x = int(pos_x)
        self.pos_y = int(pos_y)

    def picture_from_character(self, character):
        self.character = character
        return self.character


"""
Create the McGyver class out of the mother class: Character
using 'M' for McGyver
"""


class McGyver(Character):
    def __init__(self, pos_x, pos_y):
        Character.__init__(self, "M", pos_x, pos_y)

    """
    Method to learn the position
    """

    def position(self):
        return self.pos_x, self.pos_y

    def set_position(self, x, y):
        self.pos_x = x
        self.pos_y = y


"""
Create the Guardian class out of the mother class: Character
Using "G" for Guardian
"""


class Guardian(Character):
    def __init__(self, pos_x, pos_y,):
        Character.__init__(self, "G", pos_x, pos_y)
