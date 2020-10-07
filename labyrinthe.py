import re

"""
Creating a Labyrinthe class to make the maze appear as well as character's position
"""


class Labyrinthe:

    """
    init an empty list to make a list of lists later : Method parsing.
    """

    def __init__(self, name_file):
        self.structure = []
        self.file = name_file
        self.maze = []
        self.pos_perso = ["x", "y"]

    def pick_up_from_file(self):

        # I open my file and read it line per line to take out all the "o" and "t" existing inside
        with open(self.file, "r") as file:
            for content in range(15):
                line = file.readline()
                liste = re.findall("[O.]", line)
                # if my list from my line is bigger than 15 char, I reduce it to have only 15
                if len(line) == 15:
                    liste = list[:15]
                self.structure.append(liste)

    """
    I show my list of lists
    """

    def show_list(self):
        for liste in self.structure:
            print(liste)

    """
    verify if the move is possible: out of the maze or on a wall or on a path
    return None if forbidden
    """

    def autorize_move(self, pos_perso, pos_col, pos_line):
        self.n_cols = len(self.structure[0])
        self.n_line = len(self.structure)
        walls = "O"
        if (pos_line > (self.n_line - 1)) or (pos_col > (self.n_cols - 1)):
            return None
        elif pos_perso == walls:
            return None
        else:
            return [pos_col, pos_line]

    """
    To find a character's position in the maze using the slicing method.
    'pos_perso' define the exact position (x,y) of the character
    """

    def find_character_position(self, pos_perso, n_line=0):
        for line in self.structure:
            if n_line == pos_perso[1]:
                print(line[0:pos_perso])
                pos_perso += 1
            else:
                print(line)
                n_line += 1
            self.maze.append(line)
            return self.maze


map_lab = Labyrinthe("laby.txt")
map_lab.pick_up_from_file()
map_lab.show_list()
