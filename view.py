import pygame
from . import constant
from . import labyrinthe


pygame.init()

class View:

    def __init__(self):
        self.map_lab = labyrinthe.Labyrinthe("laby.txt")
        self.walls = self.map_lab.find_all("O")
        strike_player = pygame.image.load(constant.HERO_IMAGE).convert_alpha()

        window = pygame.display.set_mode(constant.SCREEN_HEIGHT, constant.SCREEN_WIDTH)
        background = pygame.image.load(constant.BACKGROUND_IMAGE).convert()
        walls = self.walls(pygame.image.load(constant.WALL_IMAGE).convert())
        # afficher l'image dans la fenetre
        window.blit(background, (0, 0))
        window.display.flip()

# Afficher le fond du labyrinthe et les murs
# update pygame

        if pygame.event.type == pygame.KEYDOWN:
                # Change les coordonnées de la position de la personne
            if pygame.event.key == pygame.K_RIGHT: nPosX += 1
            if pygame.event.key == pygame.K_LEFT: nPosX -= 1
            if pygame.event.key == pygame.K_UP: nPosY -= 1
            if pygame.event.key == pygame.K_DOWN: nPosY += 1
                # Affiche le fond, puis la personne par-dessus
            window.blit(background, (0, 0))
            window.blit(strike_player, (nPosX, nPosY))

                # Actualise la fenêtre
                pygame.display.flip()
#pygame.blit(mg.sprite, mg.position)

    def display_items(self):

import pygame

pygame.init()

window_resolution = (500, 500)
black_color = (0, 0, 0)
blue_color = (90, 124, 250)

pygame.display.set_caption("Maze : McGyver")
screen = pygame.display.set_mode(window_resolution, pygame.RESIZABLE)
strike = pygame.image.load("ressource/Gardien.png")
bg = pygame.image.load("ressource/structures.png")
x = 0
y = 0
width = 34
height = 36
velocity = 5
up = False
down = False
left = False
right = False
walkcount = 0
clock = pygame.time.Clock()

def game_window():
    global walkcount

    screen.blit(bg, [0, 0])
    if walkcount + 1 >= 27:
        walkcount = 0
    if up or down or left or right:
        screen.blit(strike, [x, y])
        walkcount += 1
    else:
        walkcount = 0

    pygame.display.update()

run = True
while run:
    clock.tick(27)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        keys = pygame.key.get_pressed()

        if keys[pygame.K_UP] and y > velocity:
            y -= velocity
        if keys[pygame.K_DOWN] and y < 480 - width - velocity:
            y += velocity
        if keys[pygame.K_LEFT] and x > velocity:
            x -= velocity
            left = True
            right = False
        if keys[pygame.K_RIGHT] and x < 640 - width - velocity:
            x += velocity
            left = False
            right = True

    game_window()



