from random import choice
from pygame import *

from characters import *
from item import *
from labyrinthe import *
from view import *
from constant import *

"""
Creating controller's class to manage the game
"""
pygame.init()


class Controller:
    def __init__(self):
        # calling classes
        self.lab = Labyrinthe("laby.txt")
        self.lab.pick_up_from_file()
        self.view = View()
        self.lab.analyze_file()
        # setting characters
        self.player = McGyver(0, 0)
        self.guardian = Guardian(14, 14)
        # setting items
        self.pipe = Items("P", -1, -1)
        self.needle = Items("N", -1, -1)
        self.ether = Items("E", -1, -1)
        self.items = []
        # setting structure's bases
        self.paths = self.lab.find_all(".")
        self.walls = self.lab.find_all("O")

    """
    Method to define a random position x,y for each of the 3 items
    """
    def set_items_positions(self):
        self.pipe.x, self.pipe.y = choice(self.paths)
        self.ether.x, self.ether.y = choice(self.paths)
        self.needle.x, self.needle.y = choice(self.paths)
        self.items = [self.pipe,
                      self.needle,
                      self.ether]

    """
    Method to retrieve items.
    If Mc Gyver x,y position is the same as one of the items: 
    - the item get in his inventory
    - the item disappear from the map 
    """
    def retrieve_items(self):
        for element in self.items:
            if (self.player.pos_y, self.player.pos_x) == (element.y, element.x):
                if not element.is_collected:
                    element.go_to_inventory()
                    self.player.collect_item(element)
                    self.lab.remove_item(element.y, element.x)

    """
    Method to set 2D for the items
    """
    def load_items(self):
        for element in self.items:
            if element == self.pipe:
                self.view.window.blit(self.view.pipe,
                                      (element.y * SPRITE_SIZE,
                                       element.x * SPRITE_SIZE))
            if element == self.needle:
                self.view.window.blit(self.view.needle,
                                      (element.y * SPRITE_SIZE,
                                       element.x * SPRITE_SIZE))
            if element == self.ether:
                self.view.window.blit(self.view.ether,
                                      (element.y * SPRITE_SIZE,
                                       element.x * SPRITE_SIZE))

    """
    Method to write a "win or loose" message depending of the achievement of Mc Gyver
    When Mc Gyver x,y position is equal to the guardian x,y position:
    - if Mc Gyver collected all of the 3 items then he won otherwise he lost.
    """
    def win_or_loose(self):
        if (self.player.pos_x, self.player.pos_y) == (self.guardian.pos_x, self.guardian.pos_y):
            if len(self.player.inventory) == 3:
                self.view.win()
            if len(self.player.inventory) != 3:
                self.view.loose()
    """
    Method to upload all the images necessary for building the maze in 2D
    """
    def upload_structure_2d(self):
        # load the background in 2D
        self.view.window.blit(self.view.background, [0, 0])
        # load the guard in 2D
        self.view.window.blit(self.view.guardian, [SCREEN_WIDTH - SPRITE_SIZE,
                                                   SCREEN_HEIGHT - SPRITE_SIZE - BANDEAU])
        # load the walls in 2D
        for element in self.walls:
            wall = self.view.wall
            self.view.window.blit(wall, [element[1] * SPRITE_SIZE, element[0] * SPRITE_SIZE])
        # load items in 2D
        for element in self.items:
            if element == self.pipe:
                self.view.window.blit(self.view.pipe, (element.y * SPRITE_SIZE, element.x * SPRITE_SIZE))
            if element == self.needle:
                self.view.window.blit(self.view.needle, (element.y * SPRITE_SIZE, element.x * SPRITE_SIZE))
            if element == self.ether:
                self.view.window.blit(self.view.ether,  (element.y * SPRITE_SIZE, element.x * SPRITE_SIZE))
        # load Mc Gyver in 2D
        self.view.window.blit(self.view.hero, [self.player.pos_x * SPRITE_SIZE, self.player.pos_y * SPRITE_SIZE])

    """
    Method to set the items and Mcg Gyver in the maze before to start the loop
    """
    def before_loop(self):
        # set and instantiate items positions
        self.set_items_positions()
        for element in self.items:
            self.lab.put_item(element.name, element.x, element.y)
        # instantiate Mc Gyver positions
        self.lab.move_player("M", self.player.pos_x, self.player.pos_y,
                             self.player.pos_x, self.player.pos_y)
        # get Mc Gyver positions
        self.lab.return_position(self.player.pos_y, self.player.pos_x)

    """
    Game loop to run the game
    """
    def loop(self):
        # instantiate pygame loop to run correctly the game and close it easily with the exit cross if wanted
        launched = True
        while launched:
            self.upload_structure_2d()
            for action in pygame.event.get():
                if action.type == pygame.QUIT:
                    launched = False
                elif action.type == pygame.KEYUP:
                    # actions of movement: if Mc gGyver moves, we change is position, set it and delete the old one
                    if action.key == pygame.K_UP and \
                                self.lab.authorize_pos(self.player.pos_y - 1, self.player.pos_x):
                        self.player.move_mcgyver("u")
                        self.lab.move_player("M", self.player.pos_y + 1, self.player.pos_x,
                                             self.player.pos_y, self.player.pos_x)

                    if action.key == pygame.K_DOWN and \
                            self.lab.authorize_pos(self.player.pos_y + 1, self.player.pos_x):
                        self.player.move_mcgyver("d")
                        self.lab.move_player("M",  self.player.pos_y - 1, self.player.pos_x,
                                             self.player.pos_y, self.player.pos_x)

                    if action.key == pygame.K_LEFT and \
                            self.lab.authorize_pos(self.player.pos_y, self.player.pos_x - 1):
                        self.player.move_mcgyver("l")
                        self.lab.move_player("M",  self.player.pos_y, self.player.pos_x + 1,
                                             self.player.pos_y, self.player.pos_x)

                    if action.key == pygame.K_RIGHT and \
                            self.lab.authorize_pos(self.player.pos_y, self.player.pos_x + 1):
                        self.player.move_mcgyver("r")
                        self.lab.move_player("M", self.player.pos_y, self.player.pos_x - 1,
                                             self.player.pos_y, self.player.pos_x)
            # pick up the items, put them in the inventory and delete their old position
            self.retrieve_items()
            # view of the inventory in 2D
            self.view.show_inventory(self.player)
            # action of wining or losing depending of the score
            self.win_or_loose()
            # refresh the pygame maze with a flip
            pygame.display.flip()


if __name__ == '__main__':
    con = Controller()
    print(con.set_items_positions())
