# coding: utf-8

import pygame

from constant import *


pygame.init()

"""
Initialize a View class to download all the images and set the texts
"""


class View:

    def __init__(self):
        # window resolution and name
        self.resolution = (SCREEN_WIDTH, SCREEN_HEIGHT)
        self.window = pygame.display.set_mode(self.resolution)
        self.title = pygame.display.set_caption(WINDOW_TITLE)
        # load structure's images
        self.background = pygame.image.load(BACKGROUND_IMAGE)
        self.band = pygame.image.load(BANDEAU_IMAGE)
        self.path = pygame.image.load(BACKGROUND_IMAGE)
        self.path = pygame.transform.scale(self.path, (30, 30))
        self.wall = pygame.image.load(WALL_IMAGE)
        # load item's images
        self.pipe = pygame.image.load(PIPE_IMAGE).convert_alpha()
        self.needle = pygame.image.load(NEEDLE_IMAGE).convert()
        self.ether = pygame.image.load(ETHER_IMAGE).convert_alpha()
        self.load_items = [self.pipe, self.needle, self.ether]
        # load character's images
        self.guardian = pygame.image.load(GUARDIAN_IMAGE).convert_alpha()
        self.hero = pygame.image.load(HERO_IMAGE).convert_alpha()

    def show_inventory(self, hero):  # message to see the collect of the items
        arial_font = pygame.font.SysFont("arial", 20)
        text = arial_font.render("You have collected {} item(s)".format(len(hero.inventory)),
                                 True, RED_COLOR)
        self.window.blit(text, [0, 450])
        pygame.display.flip()

    def win(self):  # message if you win
        arial_font = pygame.font.SysFont("arial", 50, True)
        won = arial_font.render("YOU WON!", True, BLACK_COLOR)
        self.window.blit(won, [100, 190])
        pygame.display.flip()

    def loose(self):  # message if you loose
        arial_font = pygame.font.SysFont("arial", 50, True)
        lost = arial_font.render("GAME OVER!", True, BLACK_COLOR)
        self.window.blit(lost, [100, 190])
        pygame.display.flip()
