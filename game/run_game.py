# coding: utf-8

from game.controller import *

pygame.init()

""" Class to call all the classes and condense the code for running the game """


class RunGame:
    def __init__(self):
        self.controller = Controller()

    def run_the_game(self):
        self.controller.before_loop()
        self.controller.loop()


if __name__ == '__main__':
    run = RunGame()
    run.run_the_game()
