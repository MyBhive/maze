# coding: utf-8
import pygame

from game.controller import Controller

pygame.init()


"""Import of pygame and the Controller class"""


class RunGame:
    """Class to call all the classes and
    condense the code for running the game"""
    def __init__(self):
        """Initialize the controller"""
        self.controller = Controller()

    def run_the_game(self):
        """Method to make the game working"""
        self.controller.before_loop()
        self.controller.loop()
