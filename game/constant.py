# coding: utf-8

"""Graphic and Visual elements of the maze"""


BLACK_COLOR = (0, 0, 0)
BLUE_COLOR = (90, 124, 250)
RED_COLOR = (250, 15, 30)
# Screen characteristics
NB_SPRITE_SIDE = 15
SPRITE_SIZE = 30
BANDEAU = 30
SCREEN_WIDTH = int(NB_SPRITE_SIDE * SPRITE_SIZE)
SCREEN_HEIGHT = int(NB_SPRITE_SIDE * SPRITE_SIZE + 30)
WINDOW_TITLE = "Maze : McGyver!"

# Maze images
BACKGROUND_IMAGE = "game/Ressource/background.jpg"
GUARDIAN_IMAGE = "game/Ressource/Gardien.png"
WALL_IMAGE = "game/Ressource/mur.png"
HERO_IMAGE = "game/Ressource/MacGyver.png"
NEEDLE_IMAGE = "game/Ressource/aiguille.png"
ETHER_IMAGE = "game/Ressource/ether.png"
PIPE_IMAGE = "game/Ressource/tube_plastique.png"
BANDEAU_IMAGE = "game/Ressource/black_border.png"

# 3 objects to find
NEEDLE_LETTER = "N"
PIPE_LETTER = "P"
ETHER_LETTER = "E"

# Text for the end of the game
WIN = 'You win! You can escape!'
LOOSE = "You can't escape! The guardian killed you!"
