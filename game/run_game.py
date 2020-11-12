# coding: utf-8
import pygame

from game.controller import Controller

pygame.init()


"""Import class controller and
pygame to run all together"""


class RunGame:
    """Class to call all the classes and
    condense the code for running the game"""
    def __init__(self):
        """Initialize the controller class"""
        self.controller = Controller()

    def run_the_game(self):
        """Call all what needed to run the game"""
        self.controller.before_loop()
        self.controller.loop()
