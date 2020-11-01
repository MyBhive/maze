"""Display class of McGyver Maze"""

import pygame
import constant
import labyrinthe
import controller
import characters

pygame.init()

resolution = (constant.SCREEN_WIDTH, constant.SCREEN_HEIGHT)
window = pygame.display.set_mode(resolution)
title = pygame.display.set_caption(constant.WINDOW_TITLE)

background = pygame.image.load(constant.BACKGROUND_IMAGE)
wall = pygame.image.load(constant.WALL_IMAGE)
hero = pygame.image.load(constant.HERO_IMAGE).convert_alpha()
guardian = pygame.image.load(constant.GUARDIAN_IMAGE).convert_alpha()
ether = pygame.image.load(constant.ETHER_IMAGE).convert_alpha()
pipe = pygame.image.load(constant.PIPE_IMAGE).convert_alpha()
needle = pygame.image.load(constant.NEEDLE_IMAGE).convert()

# from list to graphisme
maze = labyrinthe.Labyrinthe("laby.txt")
maze.pick_up_from_file()
walls = maze.find_all("O")

# item
con = controller.Controller()
con.set_items_positions()
objet = (ether, pipe, needle)

# mc gyver
mcky = characters.McGyver(0, 0)
mcky.pos_y = 0
mcky.pos_y = 0

# TEXTE
arial_font = pygame.font.SysFont("arial", 20)
text = arial_font.render("You have collected {} items".format(len(mcky.inventory)), True, constant.RED_COLOR)
window.blit(text, [0, 450])

pygame.display.flip()

maze.move_player(hero, mcky.pos_y, mcky.pos_x,mcky.pos_y, mcky.pos_x)

launched = True
while launched:
    # le fond
    window.blit(background, [0, 0])
# guardian
    window.blit(guardian, [constant.SCREEN_WIDTH - constant.SPRITE_SIZE,
                           constant.SCREEN_HEIGHT - constant.SPRITE_SIZE - constant.BANDEAU])

    for element in walls:
        wall = pygame.image.load(constant.WALL_IMAGE)
        window.blit(wall, [element[1] * constant.SPRITE_SIZE, element[0] * constant.SPRITE_SIZE])

# les items
    for element in con.items:
        if element == con.pipe:
            window.blit(pipe, (element.y * constant.SPRITE_SIZE, element.x * constant.SPRITE_SIZE))
        if element == con.needle:
            window.blit(needle, (element.y * constant.SPRITE_SIZE, element.x * constant.SPRITE_SIZE))
        if element == con.ether:
            window.blit(ether, (element.y * constant.SPRITE_SIZE, element.x * constant.SPRITE_SIZE))

# mcgyver
    window.blit(hero, [mcky.pos_x, mcky.pos_y])

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            launched = False
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                mcky.move_mcgyver("u")
            if event.key == pygame.K_DOWN:
                mcky.move_mcgyver("d")
            if event.key == pygame.K_LEFT:
                mcky.move_mcgyver("l")
            if event.key == pygame.K_RIGHT:
                mcky.move_mcgyver("r")
    # que mcky ne sorte pas de la fenetre
    #left
    if mcky.pos_x <= 0:
        mcky.pos_x = 0
    # right
    elif mcky.pos_x >= constant.SCREEN_WIDTH - constant.SPRITE_SIZE:
        mcky.pos_x = constant.SCREEN_WIDTH - constant.SPRITE_SIZE
    # up
    if mcky.pos_y <= 0:
        mcky.pos_y = 0
    # down
    elif mcky.pos_y >= constant.SCREEN_HEIGHT - (constant.BANDEAU + constant.SPRITE_SIZE):
        mcky.pos_y = constant.SCREEN_HEIGHT - (constant.BANDEAU + constant.SPRITE_SIZE)

    maze.authorize_position(mcky.pos_y, mcky.pos_x)
    pygame.display.flip()
