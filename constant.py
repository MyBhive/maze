
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
BACKGROUND_IMAGE = "Ressource/background.jpg"
GUARDIAN_IMAGE = "Ressource/Gardien.png"
WALL_IMAGE = "Ressource/mur.png"
HERO_IMAGE = "Ressource/MacGyver.png"
NEEDLE_IMAGE = "Ressource/aiguille.png"
ETHER_IMAGE = "Ressource/ether.png"
PIPE_IMAGE = "Ressource/tube_plastique.png"
BANDEAU_IMAGE = "Ressources/CarreNoir.png"

# 3 objects to find
NEEDLE_LETTER = "N"
PIPE_LETTER = "P"
ETHER_LETTER = "E"

# Text for the end of the game
WIN = 'You win! You can escape!'
LOOSE = "You can't escape! The guard kill you!"


