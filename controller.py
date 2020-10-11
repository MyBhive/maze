from random import choice

from minimaze.maze import labyrinthe
from minimaze.maze import view
from minimaze.maze import characters
from minimaze.maze import item


"""
Creating controller's class to manage the game
"""


class Controller:
    def __init__(self):
        self.map_lab = labyrinthe.Labyrinthe("laby.txt")
        self.player = characters.McGyver(0, 0)
        self.guardian = characters.Guardian(14, 14)
        self.keyboard = view.View.ask_user_direction
        self.direction = labyrinthe.Labyrinthe.move_mcgyver
        self.inventury = []
        # appeler tous les self nécessaire (mcgyver, items etc)
        # items: 'E' for Ether / 'N' for Needle / 'P' for Pipe
        self.items = [item.Items("E", 0, 0),
                      item.Items("N", 0, 0),
                      item.Items("P", 0, 0)]

        self.paths = self.map_lab.find_all(".")

    def set_items_positions(self):
        for element in self.items:
            # random position in the list empty_space
            position = choice(self.paths)
            # We place object on the map
            element.set_position(position[0], position[1])
            # We put three objects in a  map
            self.map_lab.pos_character(element, element.x, element.y)

    def items_to_collect(self):
        pos_items = [0, 0]
        pos_player = [0, 0]
        if pos_player == pos_items:
            self.inventury += 1
            self.items = self.paths

        return self.inventury

    def run_the_game(self):
        if self.keyboard == "Up":
            self.direction(True, False, False, False)
        if self.keyboard == "Down":
            self.direction(False, True, False, False)
        if self.keyboard == "Left":
            self.direction(False, False, True, False)
        if self.keyboard == "Right":
            self.direction(False, False, False, True)


# if position "M" == "Seringue":
# inventaire += 1
# positionseringue = "."
if __name__ == '__main__':
    controller = Controller()
    print(controller.set_items_positions())
