from random import choice

import characters
import item
import labyrinthe
import view

"""
Creating controller's class to manage the game
"""


class Controller:
    def __init__(self):
        self.lab = labyrinthe.Labyrinthe("laby.txt")
        self.map_lab = self.lab.show_maze()
        self.lab.pick_up_from_file()
        self.view = view.View()
        self.lab.analyze_file()

        self.player = characters.McGyver(0, 0, 0, 0)
        self.guardian = characters.Guardian(14, 14)

        self.pipe = "P"
        self.needle = "N"
        self.ether = "E"
        self.items = [item.Items(self.pipe, -1, -1),
                      item.Items(self.needle, -1, -1),
                      item.Items(self.ether, -1, -1)]

        self.paths = self.lab.find_all(".")
        self.walls = self.lab.find_all("O")

    def set_items_positions(self):
        self.pipe = choice(self.paths)
        self.ether = choice(self.paths)
        self.needle = choice(self.paths)
        return self.ether, self.needle, self.pipe

    def start(self):
        # instancier les positions
        self.set_items_positions()
        self.lab.put_item("E", self.ether[0], self.ether[1])
        self.lab.put_item("P", self.pipe[0], self.pipe[1])
        self.lab.put_item("N", self.needle[0], self.needle[1])
        # loop running as long as the player and guardian are not meeting
        while (self.player.pos_x, self.player.pos_y) != (self.guardian.pos_x, self.guardian.pos_y):
            # afficher les positions
            self.lab.show_maze()
            self.lab.authorize_position(self.player.pos_x, self.player.pos_y)
            self.lab.move_player("M", self.player.x_before, self.player.y_before,
                                 self.player.pos_x, self.player.pos_y)
            self.lab.return_position(self.player.pos_x, self.player.pos_y)
            to_go = self.view.ask_direction()
            # move_player de la classe character à metre directement ici
            if to_go == "u":
                self.player.move_mcgyver("u")
                self.player.before_move("u")
                self.lab.move_player("M", self.player.x_before, self.player.y_before,
                                     self.player.pos_x, self.player.pos_y)
            if to_go == "d":
                self.player.move_mcgyver("d")
                self.player.before_move("d")
                self.lab.move_player("M", self.player.x_before, self.player.y_before,
                                     self.player.pos_x, self.player.pos_y)
            if to_go == "l":
                self.player.move_mcgyver("l")
                self.player.before_move('l')
                self.lab.move_player("M", self.player.x_before, self.player.y_before,
                                     self.player.pos_x, self.player.pos_y)
            if to_go == "r":
                self.player.move_mcgyver("r")
                self.player.before_move('r')
                self.lab.move_player("M", self.player.x_before, self.player.y_before,
                                     self.player.pos_x, self.player.pos_y)
            for element in self.items:
                if self.player.position() == element:
                    if element == self.pipe:
                        self.player.collect_item(self.pipe)
                        self.lab.remove_item(self.pipe[0], self.pipe[1])
                    if element == self.needle:
                        self.player.collect_item(self.needle)
                        self.lab.remove_item(self.needle[0], self.needle[1])
                    if element == self.ether:
                        self.player.collect_item(self.ether)
                        self.lab.remove_item(self.ether[0], self.ether[1])

        if len(self.player.inventory) == 3:
            print("gagné")

        if len(self.player.inventory) < 3:
            print("perdu!")


if __name__ == '__main__':
    con = Controller()
    con.lab.pick_up_from_file()
    print(con.start())
