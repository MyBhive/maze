# coding: utf-8

import pygame
from random import choice

import game.characters as character
import game.item as it
import game.labyrinthe as lab
import game.view as view
import game.constant as cst


"""Import all the classes to make them
working together and built the game"""

pygame.init()
clock = pygame.time.Clock()


class Controller:
    """Creating controller's class to manage the game"""
    def __init__(self):
        """Initialize the import of the classes
        and the main data to be used"""
        # calling classes
        self.lab = lab.Labyrinthe("game/ressource/laby.txt")
        self.lab.pick_up_from_file()
        self.view = view.View()
        self.lab.analyze_file()
        # setting characters
        self.player = character.McGyver(0, 0)
        self.guardian = character.Guardian(14, 14)
        # setting items
        self.pipe = it.Items("P", -1, -1)
        self.needle = it.Items("N", -1, -1)
        self.ether = it.Items("E", -1, -1)
        self.items = []
        # setting structure's bases
        self.paths = self.lab.find_all(".")
        self.walls = self.lab.find_all("O")

    def set_items_positions(self):
        """Method to define a random position x,y
        for each of the 3 items"""
        self.items = [self.pipe,
                      self.needle,
                      self.ether]
        for item in self.items:
            item.y, item.x = choice(self.paths)
            # make sure it will never be 2 items at the same position
            if self.needle == self.pipe or self.ether:
                item.y, item.x = choice(self.paths)

    def load_structure_2d(self):
        """Method to upload all the images necessary
        for building the maze in 2D"""
        # load the background in 2D
        self.view.window.blit(self.view.background, [0, 0])
        self.view.window.blit(self.view.band, [0, 450])
        # load path in 2D
        for element in self.paths:
            self.view.window.blit(self.view.path,
                                  [element[1] * cst.SPRITE_SIZE,
                                   element[0] * cst.SPRITE_SIZE])
        # load the walls in 2D
        for element in self.walls:
            self.view.window.blit(self.view.wall,
                                  [element[1] * cst.SPRITE_SIZE,
                                   element[0] * cst.SPRITE_SIZE])
        # load the guard in 2D
        self.view.window.blit(self.view.guardian,
                              [cst.SCREEN_WIDTH - cst.SPRITE_SIZE,
                               cst.SCREEN_HEIGHT - cst.SPRITE_SIZE
                               - cst.BANDEAU])

        # load Mc Gyver in 2D
        self.view.window.blit(self.view.hero,
                              [self.player.pos_x * cst.SPRITE_SIZE,
                               self.player.pos_y * cst.SPRITE_SIZE])
        # load items in 2D
        for element in self.items:
            if element == self.pipe:
                self.view.window.blit(self.view.pipe,
                                      [element.x * cst.SPRITE_SIZE,
                                       element.y * cst.SPRITE_SIZE])
            if element == self.needle:
                self.view.window.blit(self.view.needle,
                                      [element.x * cst.SPRITE_SIZE,
                                       element.y * cst.SPRITE_SIZE])
            if element == self.ether:
                self.view.window.blit(self.view.ether,
                                      [element.x * cst.SPRITE_SIZE,
                                       element.y * cst.SPRITE_SIZE])

    def retrieve_items(self):
        """Method to retrieve items.
        If Mc Gyver x,y position is the same as one of the items:
        - the item get in his inventory
        - the item disappear from the map"""
        for element in self.items:
            if (self.player.pos_x, self.player.pos_y) == \
                    (element.x, element.y):
                if not element.is_collected:  # not false
                    element.go_to_inventory()  # inventory.append(item)
                    self.player.collect_item(element)  # true
                    # delete item image from the map
                    self.items.remove(element)

    def win_or_loose(self):
        """Method to write a "win or loose" message
        depending of the achievement of Mc Gyver.
        When Mc Gyver x,y position is equal
        to the guardian x,y position:
        - if Mc Gyver collected all of the 3 items
        then he won otherwise he lost."""
        final = True
        while final:
            for action in pygame.event.get():
                if action.type == pygame.QUIT:
                    final = False
            self.view.window.blit(self.view.background, [0, 0])
            if len(self.player.inventory) == 3:
                self.view.win()
            else:
                self.view.loose()

    def before_loop(self):
        """Method to set the items and Mcg Gyver
        in the maze before to start the loop"""
        # set and instantiate items positions
        self.set_items_positions()
        for element in self.items:
            self.lab.put_item(element.name,
                              element.x,
                              element.y)

    def loop(self):
        """Game loop to run the game :
        instantiate pygame loop to run correctly the game
        and close it easily with the exit cross if wanted"""
        launched = True
        while launched:
            self.load_structure_2d()
            # get Mc Gyver positions
            self.lab.return_position(self.player.pos_y,
                                     self.player.pos_x)
            for action in pygame.event.get():
                if action.type == pygame.QUIT:
                    launched = False
                elif action.type == pygame.KEYUP:
                    # actions of movement:
                    # press an arrow's keyboard to actuate a move
                    if action.key == pygame.K_UP:
                        # to block the move if out of a path
                        if self.lab.authorize_pos(self.player.pos_y - 1,
                                                  self.player.pos_x):
                            # visibility of the action of movement
                            self.player.move_mcgyver("u")

                    if action.key == pygame.K_DOWN:
                        if self.lab.authorize_pos(self.player.pos_y + 1,
                                                  self.player.pos_x):
                            self.player.move_mcgyver("d")

                    if action.key == pygame.K_LEFT:
                        if self.lab.authorize_pos(self.player.pos_y,
                                                  self.player.pos_x - 1):
                            self.player.move_mcgyver("l")

                    if action.key == pygame.K_RIGHT:
                        if self.lab.authorize_pos(self.player.pos_y,
                                                  self.player.pos_x + 1):
                            self.player.move_mcgyver("r")

            # when the player meet the guardian: screen win or loose the game
            if (self.player.pos_x, self.player.pos_y) == (self.guardian.pos_x,
                                                          self.guardian.pos_y):
                launched = False
                self.win_or_loose()
            # pick up the items, put them in the inventory
            # and delete their old position
            self.retrieve_items()
            # view of the inventory in 2D
            self.view.show_inventory(self.player)
            # frame time: to have the same speed (image per second)
            # whatever the computer used
            clock.tick(30)
