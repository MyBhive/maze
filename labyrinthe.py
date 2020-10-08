import re

"""
Creating a Labyrinthe's class to make the maze appear as well as character's position
"""


class Labyrinthe:

    """
    init an empty list to make a list of lists later : Method parsing.
    """

    def __init__(self, name_file):
        self.map_structure = []
        self.file = name_file

    def pick_up_from_file(self):
        # I open my file and read it line per line to take out all the "o" and "t" existing inside
        with open(self.file, "r") as file:
            for content in range(15):
                line = file.readline()
                liste = re.findall("[MGO.]", line)
                # if my list from my line is bigger than 15 char, I reduce it to have only 15
                if len(line) == 15:
                    liste = list[:15]
                self.map_structure.append(liste)

    """
    I show my list of lists
    """

    def show_list(self):
        for line in self.map_structure:
            print(line)

    """
    verify if the move is possible: out of the maze, or, on a wall, or, on a path
    return None if forbidden
    """

    def autorize_move(self, pos_col, pos_line):
        self.n_col = len(self.map_structure[0])
        self.n_line = len(self.map_structure)
        walls = "O"
        paths = "."
        if pos_line and pos_col == paths:
            return [pos_col, pos_line]
        if pos_line < 0 or pos_col < 0 or pos_line > (self.n_line - 1) or pos_col > (self.n_col - 1):
            return None
        elif self.map_structure[pos_line][pos_col] == walls:
            return None


    """
    Method to attribute the position line x and position column y to the character
    """

    def pos_perso(self, character, x, y):
        self.map_structure[x][y] = character

    """
    Method to find a character's position in the maze using the slicing method.
    'pos_perso' define the exact position (x,y) of the character
    """

    def find_character_position(self, character):
        # list of position x and y of one character
        localisation = []
        n_line = 0
        pos_perso = [0]
        for line in self.map_structure:
            if n_line == pos_perso[1]:
                print(line[0:pos_perso] + character + line[pos_perso[0]+1:])
            else:
                print(line)
                n_line += 1
            localisation.append(line)
        return localisation

    """
    Method which return the position of the character in the maze
    """

    def return_position(self, x, y):
        character = self.map_structure[x][y]
        return character
