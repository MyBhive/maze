# coding: utf-8
import pygame

from game.controller import Controller

pygame.init()

""" Class to call all the classes and condense the code for running the game """


class RunGame:
    def __init__(self):
        self.controller = Controller()

    def run_the_game(self):
        self.controller.before_loop()
        self.controller.loop()

