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
        self.lab.pick_up_from_file()
        self.view = view.View()
        self.lab.analyze_file()

        self.player = characters.McGyver(0, 0)
        self.guardian = characters.Guardian(14, 14)

        self.pipe = item.Items("P", -1, -1)
        self.needle = item.Items("N", -1, -1)
        self.ether = item.Items("E", -1, -1)
        self.items = []

        self.paths = self.lab.find_all(".")
        self.walls = self.lab.find_all("O")

    def set_items_positions(self):
        self.pipe.x, self.pipe.y = choice(self.paths)
        self.ether.x, self.ether.y = choice(self.paths)
        self.needle.x, self.needle.y = choice(self.paths)
        self.items = [self.pipe,
                      self.needle,
                      self.ether]

    def start(self):
        # instancier les positions
        self.set_items_positions()
        
        for element in self.items:
            self.lab.put_item(element.name, element.x, element.y)
                              
        self.lab.move_player("M", self.player.pos_x, self.player.pos_y,
                             self.player.pos_x, self.player.pos_y)
        # loop running as long as the player and guardian are not meeting
        while (self.player.pos_x, self.player.pos_y) != (self.guardian.pos_x, self.guardian.pos_y):
            # afficher les positions
            self.lab.show_maze()
            self.lab.return_position(self.player.pos_x, self.player.pos_y)
            to_go = self.view.ask_direction()
            # move_player de la classe character à metre directement ici
            if to_go == "u" and self.lab.authorize_position(self.player.pos_x - 1, self.player.pos_y):
                self.player.move_mcgyver("u")
                self.lab.move_player("M", self.player.pos_x + 1, self.player.pos_y,
                                     self.player.pos_x, self.player.pos_y)
            if to_go == "d" and self.lab.authorize_position(self.player.pos_x + 1, self.player.pos_y):
                self.player.move_mcgyver("d")
                self.lab.move_player("M", self.player.pos_x - 1, self.player.pos_y,
                                     self.player.pos_x, self.player.pos_y)
            if to_go == "l" and self.lab.authorize_position(self.player.pos_x, self.player.pos_y - 1):
                self.player.move_mcgyver("l")
                self.lab.move_player("M", self.player.pos_x, self.player.pos_y + 1,
                                     self.player.pos_x, self.player.pos_y)
            if to_go == "r" and self.lab.authorize_position(self.player.pos_x, self.player.pos_y + 1):
                self.player.move_mcgyver("r")
                self.lab.move_player("M", self.player.pos_x, self.player.pos_y - 1,
                                     self.player.pos_x, self.player.pos_y)
            
            for element in self.items:
                if (self.player.pos_x, self.player.pos_y) == (element.x, element.y):
                    if not element.is_collected:
                        element.go_to_inventory()
                        self.player.collect_item(element)
                        self.lab.remove_item(element.x, element.y)

        if len(self.player.inventory) == 3:
            print("you won !!")

        if len(self.player.inventory) != 3:
            print("game over !")


if __name__ == '__main__':
    con = Controller()
    print(con.set_items_positions())
    print(con.start())
    print((len(con.player.inventory)))
