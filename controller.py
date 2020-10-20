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
        self.map_lab.analyze_file()
        (x_start, y_start) = self.map_lab.find_one_character("M")
        self.player = characters.McGyver(x_start, y_start)
        (x_end, y_end) = self.map_lab.find_one_character("G")
        self.guardian = characters.Guardian(x_end, y_end)
        self.inventory = []
        self.pipe = "P"
        self.needle = "N"
        self.ether = "E"
        self.items = [item.Items("E", 0, 0),
                      item.Items("N", 0, 0),
                      item.Items("P", 0, 0)]
        self.paths = self.map_lab.find_all(".")

    def set_items_positions(self):
        self.pipe = choice(self.paths)
        self.ether = choice(self.paths)
        self.needle = choice(self.paths)
        self.map_lab.find_one_character("E")
        self.map_lab.find_one_character("N")
        self.map_lab.find_one_character("P")
        return self.ether, self.needle, self.pipe

    def item_position(self):
        return self.ether, self.needle, self.pipe

    def start(self):
        self.map_lab.find_one_character("M")
        self.map_lab.find_one_character("G")
        self.item_position()
        # tant que mcgyver et le gardien ont des position différentes
        while (self.player.pos_x, self.player.pos_y) != (self.guardian.pos_x, self.guardian.pos_y):
            print(self.map_lab)
            item.Items.set_position(self.items)
            self.player.position()
            self.guardian.position()
            self.map_lab.autorize_move(self.player.pos_x, self.player.pos_y)
            self.player.move_mcgyver("K_UP")
            for element in self.items:
                if self.player.position() == element:
                    self.inventory += 1
                    self.items = self.paths

        if len(self.inventory) == 3:
            self.map_lab.find_one_character("M")
            print("gagné")

        if len(self.inventory) < 3:
            self.map_lab.find_one_character("M")
            print("perdu!")


if __name__ == '__main__':
    con = Controller()
    print(con.set_items_positions())
    print(con.start())
