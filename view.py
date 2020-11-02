import pygame
from constant import *


pygame.init()

"""
Initialize a View class to download all the images and set the texts
"""
class View:

    def __init__(self):
        self.resolution = (SCREEN_WIDTH, SCREEN_HEIGHT)
        self.window = pygame.display.set_mode(self.resolution)
        self.title = pygame.display.set_caption(WINDOW_TITLE)

        self.background = pygame.image.load(BACKGROUND_IMAGE)
        self.wall = pygame.image.load(WALL_IMAGE)
        self.pipe = pygame.image.load(PIPE_IMAGE).convert_alpha()
        self.needle = pygame.image.load(NEEDLE_IMAGE).convert()
        self.ether = pygame.image.load(ETHER_IMAGE).convert_alpha()
        self.guardian = pygame.image.load(GUARDIAN_IMAGE).convert_alpha()
        self.hero = pygame.image.load(HERO_IMAGE).convert_alpha()
        self.load_images = [self.background, self.wall, self.pipe, self.needle, self.ether, self.guardian, self.hero]
        self.load_items = [self.pipe, self.needle, self.ether]

    def show_inventory(self, hero):
        arial_font = pygame.font.SysFont("arial", 20)
        text = arial_font.render("You have collected {} items".format(len(hero.inventory)),
                                 True, RED_COLOR)
        self.window.blit(text, [0, 450])

    def win(self):
        arial_font = pygame.font.SysFont("arial", 50, True)
        won = arial_font.render("YOU WON!", True, BLACK_COLOR)
        self.window.blit(won, [100, 190])

    def loose(self):
        arial_font = pygame.font.SysFont("arial", 50, True)
        lost = arial_font.render("GAME OVER!", True, BLACK_COLOR)
        self.window.blit(lost, [100, 190])

