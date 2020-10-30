"""Display class of McGyver Maze"""

import pygame
import constant
import item
import sys
import labyrinthe
import controller

pygame.init()
pygame.font.init()

resolution = (constant.SCREEN_WIDTH, constant.SCREEN_HEIGHT)
window = pygame.display.set_mode(resolution)
title = pygame.display.set_caption(constant.WINDOW_TITLE)

background = pygame.image.load(constant.BACKGROUND_IMAGE)
wall = pygame.image.load(constant.WALL_IMAGE)
hero = pygame.image.load(constant.HERO_IMAGE).convert_alpha()
guardian = pygame.image.load(constant.GUARDIAN_IMAGE).convert_alpha()
ether = pygame.image.load(constant.ETHER_IMAGE).convert_alpha()
pipe = pygame.image.load(constant.PIPE_IMAGE).convert_alpha()
needle = pygame.image.load(constant.NEEDLE_IMAGE).convert_alpha()

# TEXTE
arial_font = pygame.font.SysFont("arial", 20)
text = arial_font.render("{}".format(constant.WINDOW_TITLE), True, constant.RED_COLOR)
window.blit(text, [0, 450])

hero_x = 0
hero_y = 0

# from list to graphisme
maze = labyrinthe.Labyrinthe("laby.txt")
maze.pick_up_from_file()
walls = maze.find_all("O")

# item in maze ne marche pas
con = controller.Controller()
con.set_items_positions()
objet = (con.pipe, con.ether, con.needle)
for element in objet:
    con.pipe = pygame.image.load(constant.PIPE_IMAGE).convert_alpha()
    window.blit(con.pipe, [element[1] * constant.SPRITE_SIZE, element[0] * constant.SPRITE_SIZE])
    con.needle = pygame.image.load(constant.NEEDLE_IMAGE).convert_alpha()
    window.blit(con.needle, [element[1] * constant.SPRITE_SIZE, element[0] * constant.SPRITE_SIZE])
    con.ether = pygame.image.load(constant.ETHER_IMAGE).convert_alpha()
    window.blit(con.ether, [element[1] * constant.SPRITE_SIZE, element[0] * constant.SPRITE_SIZE])

pygame.display.flip()

launched = True
while launched:
    # le fond
    window.blit(background, [0, 0])
    window.blit(guardian, [constant.SCREEN_WIDTH - constant.SPRITE_SIZE,
                           constant.SCREEN_HEIGHT - constant.SPRITE_SIZE - constant.BANDEAU])
    for element in walls:
        wall = pygame.image.load(constant.WALL_IMAGE)
        window.blit(wall, [element[1] * constant.SPRITE_SIZE, element[0] * constant.SPRITE_SIZE])

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            launched = False
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                hero_y -= 30
            if event.key == pygame.K_DOWN:
                hero_y += 30
            if event.key == pygame.K_LEFT:
                hero_x -= 30
            if event.key == pygame.K_RIGHT:
                hero_x += 30
    # que mcky ne sorte pas de la fenetre
    if hero_x <= 0:
        hero_x = 0
    elif hero_x >= constant.SCREEN_WIDTH - 30:
        hero_x = constant.SCREEN_WIDTH - 30
    if hero_y <= 0:
        hero_y = 0
    elif hero_y >= constant.SCREEN_HEIGHT - (30 + constant.SPRITE_SIZE):
        hero_y = constant.SCREEN_HEIGHT - (30 + constant.SPRITE_SIZE)

    window.blit(hero, [hero_x, hero_y])
    pygame.display.flip()

