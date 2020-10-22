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
    def __init__(self, pos_x, pos_y, x_before, y_before):
        super().__init__("M", pos_x, pos_y)
        self.inventory = []
        self.x_before = x_before
        self.y_before = y_before
        self.pos_x = pos_x
        self.pos_y = pos_y
    """
    Method to learn the position
    """

    def position(self):
        return self.pos_x, self.pos_y

    def move_mcgyver(self, direction):
        if direction == "u":
            self.pos_x -= 1
            return self.pos_x, self.pos_y
        elif direction == "d":
            self.pos_x += 1
            return self.pos_x, self.pos_y
        if direction == "l":
            self.pos_y -= 1
            return self.pos_x, self.pos_y
        elif direction == "r":
            self.pos_y += 1
            return self.pos_x, self.pos_y
        else:
            return False

    def before_move(self, direction):
        if direction == "u":
            self.x_before += 1
            return self.x_before, self.y_before
        elif direction == "d":
            self.x_before -= 1
            return self.x_before, self.y_before
        if direction == "l":
            self.y_before += 1
            return self.x_before, self.y_before
        elif direction == "r":
            self.y_before -= 1
            return self.x_before, self.y_before
        else:
            return False

    """
    To collect item and add it in the inventory
    """
    def collect_item(self, item):
        self.inventory.append(item)


"""
Create the Guardian class out of the mother class: Character
Using "G" for Guardian
"""


class Guardian(Character):
    def __init__(self, pos_x, pos_y,):
        super().__init__("G", pos_x, pos_y)

    def position(self):
        return self.pos_x, self.pos_y
