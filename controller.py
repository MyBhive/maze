from random import choice

import characters
import item
import labyrinthe


"""
Creating controller's class to manage the game
"""


class Controller:
    def __init__(self):
        self.map_lab = labyrinthe.Labyrinthe("laby.txt")
        self.map_lab.pick_up_from_file()
        self.map_lab.show_list()
        self.map_lab.analyze_file()
        self.player = characters.McGyver("M", 0, 0)
        self.guardian = characters.Guardian("G", 14, 14)
        self.inventory = []
        self.pipe = "P"
        self.needle = "N"
        self.ether = "E"
        self.items = [item.Items(self.pipe, 0, 0),
                      item.Items(self.needle, 0, 0),
                      item.Items(self.ether, 0, 0)]
        self.paths = self.map_lab.find_all(".")

    def set_items_positions(self):
        self.pipe = choice(self.paths)
        self.ether = choice(self.paths)
        self.needle = choice(self.paths)
        return self.ether, self.needle, self.pipe

    def item_position(self):
        return self.ether, self.needle, self.pipe

    def start(self):
        self.map_lab.write_character("M", 0, 0)
        self.map_lab.write_character("G", 14, 14)
        # loop running as long as the player and guardian are not meeting
        while (self.player.pos_x, self.player.pos_y) != (self.guardian.pos_x, self.guardian.pos_y):
            print(self.map_lab)
            self.player.position()
            self.guardian.position()
            self.item_position()
            self.map_lab.authorize_move(self.player.pos_x, self.player.pos_y)
            if self.player.move_mcgyver("K_UP"):
                return self.player.position()
            if self.player.move_mcgyver("K_DOWN"):
                return self.player.position()
            if self.player.move_mcgyver("K_LEFT"):
                return self.player.position()
            if self.player.move_mcgyver("K_RIGHT"):
                return self.player.position()
            for element in self.items:
                if self.player.position() == element:
                    self.inventory += 1
                    self.items = self.paths
            break

        if len(self.inventory) == 3:
            self.map_lab.find_one_character("M")
            print("gagné")

        if len(self.inventory) < 3:
            self.map_lab.find_one_character("M")
            print("perdu!")


if __name__ == '__main__':
    con = Controller()
    con.map_lab.pick_up_from_file()
    print(con.item_position())
    print(con.start())
