from random import choice

from .import characters
from .import item
from .import labyrinthe
from .import view

"""
Creating controller's class to manage the game
"""


class Controller:
    def __init__(self):
        self.map_lab = labyrinthe.Labyrinthe("laby.txt")
        (x_start, y_start) = self.map_lab.find_one_character("M")
        self.player = characters.McGyver(x_start, y_start)
        (x_end, y_end) = self.map_lab.find_one_character("G")
        self.guardian = characters.Guardian(x_end, y_end)
        self.inventory = []
        self.items = [item.Items("E", 0, 0),
                      item.Items("N", 0, 0),
                      item.Items("P", 0, 0)]
        self.paths = self.map_lab.find_all(".")
        self.view = view.View()

    def set_items_positions(self):
        for element in self.items:
            # random position in the list empty_space
            position = choice(self.paths)
            # We place object on the map
            element.set_position(position[0], position[1])
            # We put three objects in a  map
            self.map_lab.pos_character(element, element.x, element.y)

    def start(self):
        self.map_lab.pos_character("M", self.player.pos_x, self.player.pos_y)
        self.map_lab.pos_character("G", self.guardian.pos_x, self.guardian.pos_y)
        self.items.set_items_positions("E")
        self.items.set_items_positions("N")
        self.items.set_items_positions("P")
        # tant que mcgyver et le gardien ont des position différentes
        while (self.player.pos_x, self.player.pos_y) != (self.guardian.pos_x, self.guardian.pos_y):
            print(self.map_lab)
            self.items.set_items_positions(self.paths)
            self.player.position()
            self.guardian.position()
            (pos_x_moving, pos_y_moving) = self.player.move_mcgyver
            if self.player.move_mcgyver() != self.map_lab.autorize_move(self.player.pos_x, self.player.pos_y):
                self.map_lab.pos_character("M", pos_x_moving, pos_y_moving)
                for element in self.items:
                    if self.player.position() == element:
                        self.inventory += 1
                        self.items = self.paths

        if len(self.inventory) == 3:
            self.map_lab.pos_character("M", self.player.pos_x, self.player.pos_y)
            print("gagné")

        if len(self.inventory) < 3:
            self.map_lab.pos_character("M", self.player.pos_x, self.player.pos_y)
            print("perdu!")
