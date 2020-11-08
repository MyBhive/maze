# coding: utf-8

"""
Creating a Labyrinthe's class to make the maze appear as well as character's position
"""


class Labyrinthe:

    """ To initialize an empty list to make a list of lists."""

    def __init__(self, name_file):
        self.map_structure = []
        self.file = name_file

    """
    Method to open a file and read it line per line
    to extract all the "O" and "." existing inside
    """
    def pick_up_from_file(self):
        with open(self.file, "r") as file:
            for content in range(15):
                line = file.readline()
                liste = list(map(str, line))[:15]
                # if my list from my line is bigger than 15 char, I reduce it to have only 15
                self.map_structure.append(liste)
    """
    Method to verify if the data in my export file are correct : 
    We need to have only the hero(M), the guardian(G), 
    the walls(O), the paths(.) and the items(E,P,N)
    """

    def analyze_file(self):
        nb_of_mcgyver = 0
        nb_of_guardian = 0
        nb_of_pipe = 0
        nb_of_needle = 0
        nb_of_ether = 0
        for index_line, line in enumerate(self.map_structure):
            for index_element, element in enumerate(line):
                if element not in ["M", "G", "E", "P", "N", "O", "."]:
                    raise ValueError("Error in the text file at the line:"
                                     + str(index_line + 1)
                                     + ", the column"
                                     + str(index_element + 1)
                                     + ". Item"
                                     + element
                                     + "not allowed")
                else:
                    if element == "M":
                        nb_of_mcgyver += 1
                        if nb_of_mcgyver > 1:
                            raise ValueError(
                                "Error : you should have just 1 Mcgyver!"
                            )
                    if element == "G":
                        nb_of_guardian += 1
                        if nb_of_guardian > 1:
                            raise ValueError(
                                "Error : you should have just 1 Guardian!"
                            )
                    if element == "P":
                        nb_of_pipe += 1
                        if nb_of_pipe > 1:
                            raise ValueError(
                                "Error : you should have just 1 Pipe!"
                            )
                    if element == "E":
                        nb_of_ether += 1
                        if nb_of_ether > 1:
                            raise ValueError(
                                "Error : you should have just 1 Ether!"
                            )
                    if element == "N":
                        nb_of_needle += 1
                        if nb_of_needle > 1:
                            raise ValueError(
                                "Error : you should have just 1 Needle!"
                            )

    """ Method too show my list of lists: structure of the maze """

    def show_maze(self):
        for line in self.map_structure:
            print(line)

    """
     Method to verify if the move is possible: 
     if out of the maze --> return False
     if in a wall --> return False
     otherwise --> return True
    """

    def authorize_pos(self, pos_col, pos_line):
        wall = "O"
        line_size = len(self.map_structure[0]) - 1
        column_size = len(self.map_structure) - 1
        if (pos_line > line_size) or (pos_col > column_size):
            return False
        if (pos_line < 0) or (pos_col < 0):
            return False
        if self.map_structure[pos_col][pos_line] == wall:
            return False
        else:
            return True

    """ Method which return the position of the character in the maze """
    def return_position(self, x, y):
        character = self.map_structure[x][y]
        return character

    """ Method which put the items in the maze. 
    We take a path area and we place the item instead.
    """
    def put_item(self, character, x, y):
        if self.map_structure[x][y] == ".":
            self.map_structure[x][y] = character

    """ To find all things from one category like paths or walls """

    def find_all(self, character):
        # list of position
        positions = []
        # enumerate returns 2 variables. the first one for the line and second for the column
        for x, line in enumerate(self.map_structure):
            for y, column in enumerate(line):
                if character == column:
                    positions.append((x, y))
        return positions
