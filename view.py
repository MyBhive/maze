
"""
This class has been creatin to handle all the input() and print() in order to make the readability of the game easier
"""


class View:

    def __init__(self, character, items):
        self.character = character
        self.items = items

    rules = "Hi! Help McGyver to escape the maze. " \
            "Don't forget to collect all the 3 items before to arrive in front of the Guardian. " \
            "You need them to built a syringue to asleep the Guardian. " \
            "Otherwise you will no be abble to escape and he will kill you! Good luck!"
    choice = input("To move select: "
                   "'u'for going up/'d' for going down/'l' for going left/'r' for going right "
                   "or you can quite the game with 'Q':")
    game_over = " Aouch, you arrived in front of the Guardian without all your items! You are dead!!"
    win = "Congratulation you saved McGyver!"
    quit_or_play = input("Press 'R' to (re)start or 'Q' to Quit:")
