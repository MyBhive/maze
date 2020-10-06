
class View:

    def __init__(self,hero, items):
        self.hero = hero
        self.items = items

    choice = input("To move select: 'up'/'down'/'left'/'right' or you can quite the game with 'Q':")
    forbidden = print("déplacement impossible")

    def game_over(self):
        return " Aouch, you arrived in front of the Guardian without all your items! he killed you!"

    def win(self):
        return "Congratulation you saved McGyver!"

    def rules(self):
        return "Help McGyver to escape the maze. Don't forget to collect all what he needs before to arrive in front of the Guardian or he will kill you! Good luck!"

    def quit_or_play(self):
        return input("Press 'R' to start or 'Q' to Quit:")
