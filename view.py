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



