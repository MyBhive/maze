
"""
This class has been creating to handle all the input() and print() in order to make the readability of the game easier
"""


class View:

    def __init__(self, character, items):
        self.character = character
        self.items = items

    def rules_from_the_game(self):
        print("Hi! Help McGyver to escape the maze. "
              "Don't forget to collect all the 3 items before to arrive in front of the Guardian. "
              "You need them to built a syringue to asleep the Guardian. "
              "Otherwise you will no be abble to escape and he will kill you! Good luck!")

    def game_over(self):
        print(" Aouch, you arrived in front of the Guardian without all your items! You are dead!!")

    def win(self):
        print("Congratulation you saved McGyver!")

    def qui_or_play(self):
        quit_or_play = input("Press 'R' to (re)start or 'Q' to Quit:")
        return quit_or_play

    def ask_user_direction(self):
        keyboard = input("To move McGyver in the maze press:"
                         " 'u' for up/'d' for down/'l' for left"
                         "/'r' for right or you can quite the game with 'Q':")
        return keyboard

    def display_maze(self):
        game = Labyrinthe

# Pas d'affichage sauf dans la classe view : from class characters

