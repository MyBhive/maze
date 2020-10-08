
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

    def pic_from_character(self, character):
        self.character = character
        return self.character


"""
Create the McGyver class out of the mother class: Character
using 'M' for McGyver
"""


class McGyver(Character):
    def __init__(self, pos_x, pos_y):
        Character.__init__(self, "M", pos_x, pos_y)
        self.inventury = []
    """
    keys of movement are: 'U' for up / 'D' for down / 'L' for left and 'R' for right
    """

    def to_move(self):
        keyboard = input("To move McGyver in the maze press:"
                         " 'u' for up/'d' for down/'l' for left"
                         "/'r' for right or you can quite the game with 'Q':")
        if keyboard == 'u':
            self.pos_x -= 1
            return self.pos_x, self.pos_y
        elif keyboard == 'd':
            self.pos_x += 1
            return self.pos_x, self.pos_y
        if keyboard == 'l':
            self.pos_y -= 1
            return self.pos_x, self.pos_y
        elif keyboard == 'r':
            self.pos_y += 1
            return self.pos_x, self.pos_y
        # if something else is used
        else:
            print("please us  'u' for up/'d' for down/'l' for left""/'r' for right"
                  " or you can quite the game with 'Q' ")
            return self.pos_x, self.pos_y

    """
    Method to learn the position
    """

    def position(self):
        return self.pos_x, self.pos_y


"""
Create the Guardian class out of the mother class: Character
Using "G" for Guardian
"""


class Guardian(Character):
    def __init__(self, pos_x, pos_y,):
        Character.__init__(self, "G", pos_x, pos_y)
