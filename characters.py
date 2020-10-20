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

    """
       To define the movement of mcgyver
    """
    def move_mcgyver(self, direction):
        pos_x = 0
        pos_y = 0
        if direction == "K_UP":
            pos_x -= 1
            return pos_x, pos_y
        elif direction == "K_DOWN":
            pos_x += 1
            return pos_x, pos_y
        if direction == "K_LEFT":
            pos_y -= 1
            return pos_x, pos_y
        elif direction == "K_RIGHT":
            pos_y += 1
            return pos_x, pos_y
        else:
            return False


"""
Create the Guardian class out of the mother class: Character
Using "G" for Guardian
"""


class Guardian(Character):
    def __init__(self, pos_x, pos_y,):
        Character.__init__(self, "G", pos_x, pos_y)

    def position(self):
        return self.pos_x, self.pos_y




if __name__ == '__main__':
    ch = McGyver(0, 0)
    lt = ch.move_mcgyver("K_DOWN")
    print(lt)
    lt = ch.move_mcgyver("K_LEFT")
    print(lt)
