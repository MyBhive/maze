from random import choice
import pygame
from minimaze.maze import labyrinthe
from minimaze.maze import view
from minimaze.maze import characters
from minimaze.maze import item

'''Graphic and Visual elements of the maze'''

# Screen characteristics
nb_of_sprite = 15
sprite_size = 30
border_size = 30
screen_high = nb_of_sprite * sprite_size + border_size
screen_with = nb_of_sprite * sprite_size
window_title = pygame.display.set_caption("Maze : McGyver!")


# base
background = pygame.image.load("Ressource/background.jpg")
wall_image = pygame.image.load("Ressource/mur.png")
# characters
hero_image = pygame.image.load("Ressource/MacGyver.png").convert_alpha()
guardian = pygame.image.load("Ressource/Gardien.png").convert_alpha()
# items
needle_image = pygame.image.load("Ressource/aiguille.png").convert_alpha()
ether_image = pygame.image.load("Ressource/ether.png").convert_alpha()
pipe_image = pygame.image.load("Ressource/tube_plastique.png").convert_alpha()


"""
Creating controller's class to manage the game
"""


class Controller:
    def __init__(self):
        self.map_lab = labyrinthe.Labyrinthe("laby.txt")
        (x_start, y_start) = self.map_lab.find_one_character("M")
        self.player = characters.McGyver(x_start, y_start)
        (x_end, y_end) = self.map_lab.find_one_character("G")
        self.guardian = characters.Guardian(x_end, y_end)
        self.inventory = []
        self.items = [item.Items(ether_image, 0, 0),
                      item.Items(needle_image, 0, 0),
                      item.Items(pipe_image, 0, 0)]
        self.paths = self.map_lab.find_all(".")

    def set_items_positions(self):
        for element in self.items:
            # random position in the list empty_space
            position = choice(self.paths)
            # We place object on the map
            element.set_position(position[0], position[1])
            # We put three objects in a  map
            self.map_lab.pos_character(element, element.x, element.y)

    def start(self):
        print(self.map_lab)
        # tant que mcgyver et le gardien ont des position différentes
        while self.player != self.guardian:
            # j'appelle la carte
            print(self.map_lab)
            Controller.set_items_positions(self.paths)
            # j'appelle position mcgyver au début
            self.map_lab.pos_character(hero_image, self.player.pos_x, self.player.pos_y)
            # j'écrit la position du héro
            pos_x, pos_y = self.player.position()
            # methode de mouvement
            pos_x_moving, pos_y_moving = self.player.move_mcgyver()
            # methode de mouvement autorisé
            if self.player != self.map_lab.autorize_move(self.player.pos_x, self.player.pos_y):
                if self.player == self.items:
                    self.inventory += 1
                    self.items = self.paths
            if len(self.inventory) == 3 and self.player == self.guardian:
                view.View.win()
            if len(self.inventory) < 3 and self.player == self.guardian:
                view.View.game_over()











