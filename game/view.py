# coding: utf-8

import pygame

import game.constant as cst


pygame.init()

"""Import pygame and the constant to built the graph part"""


class View:
    """Initialize a View class
    to download all the images and set the texts"""
    def __init__(self):
        """Load all the pictures needed for 2D"""
        # window resolution and name
        self.resolution = (cst.SCREEN_WIDTH, cst.SCREEN_HEIGHT)
        self.window = pygame.display.set_mode(self.resolution)
        self.title = pygame.display.set_caption(cst.WINDOW_TITLE)
        # load structure's images
        self.background = pygame.image.load(cst.BACKGROUND_IMAGE)
        self.band = pygame.image.load(cst.BANDEAU_IMAGE)
        self.path = pygame.image.load(cst.BACKGROUND_IMAGE)
        self.path = pygame.transform.scale(self.path, (30, 30))
        self.wall = pygame.image.load(cst.WALL_IMAGE)
        # load item's images
        self.pipe = pygame.image.load(cst.PIPE_IMAGE).convert_alpha()
        self.needle = pygame.image.load(cst.NEEDLE_IMAGE).convert()
        self.ether = pygame.image.load(cst.ETHER_IMAGE).convert_alpha()
        self.load_items = [self.pipe,
                           self.needle,
                           self.ether]
        # load character's images
        self.guardian = pygame.image.load(cst.GUARDIAN_IMAGE).convert_alpha()
        self.hero = pygame.image.load(cst.HERO_IMAGE).convert_alpha()

    def show_inventory(self, hero):
        """Message to see the collect of the items"""
        arial_font = pygame.font.SysFont("arial", 20)
        text = arial_font.render("You have collected {} item(s)".
                                 format(len(hero.inventory)),
                                 True,
                                 cst.RED_COLOR)
        self.window.blit(text, [0, 450])
        pygame.display.flip()

    def win(self):
        """Message if you win"""
        arial_font = pygame.font.SysFont("arial", 50, True)
        won = arial_font.render("YOU WON!", True, cst.BLACK_COLOR)
        self.window.blit(won, [100, 190])
        pygame.display.flip()

    def loose(self):
        """Message if you loose"""
        arial_font = pygame.font.SysFont("arial", 50, True)
        lost = arial_font.render("GAME OVER!", True, cst.BLACK_COLOR)
        self.window.blit(lost, [100, 190])
        pygame.display.flip()
