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
        super(labyrinthe).__init__()
        super(view).__init__()
        super(characters).__init__()
        super(item).__init__()
        super(characters).__init__()
        self.map_lab = labyrinthe.Labyrinthe("laby.txt")
        # items: 'E' for Ether / 'N' for Needle / 'P' for Pipe
        self.items = [item.Items("E", 0, 0),
                      item.Items("N", 0, 0),
                      item.Items("P", 0, 0)] #quels positier instancier???
        # looking for paths to set the items
        self.paths = labyrinthe.Labyrinthe.show_list(".")
        # random position for item
    def set_items(self):
        for item in self.items:
            item = choice(self.items)
            position = choice(self.paths)
            item = position
        #c'est nul je sais! j'y travaille


    def run_the_game(self):
        while characters.McGyver != characters.Guardian:
            labyrinthe.Labyrinthe.show_list()
            characters.McGyver.position()
            # if mcgyver position == guardien position:
                #if item == 3 donc gagné
            # if item != 3 donc perdu
            # input rejouer ou quitter et relancer le jeu au zéro.
