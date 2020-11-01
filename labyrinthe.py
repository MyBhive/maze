
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
                liste = list(map(str, line))[:15]
                # if my list from my line is bigger than 15 char, I reduce it to have only 15
                self.map_structure.append(liste)
    """
    To verify that the data in my export file are correct
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
                    raise ValueError("Error in the text file at the line:" + str(index_line + 1) +
                                     ", the column" + str(index_element + 1) +
                                     ". Item" + element + "not allowed")
                else:
                    if element == "M":
                        nb_of_mcgyver += 1
                        if nb_of_mcgyver > 1:
                            raise ValueError("Error : you should have just 1 Mcgyver!")
                    if element == "G":
                        nb_of_guardian += 1
                        if nb_of_guardian > 1:
                            raise ValueError("Error : you should have just 1 Guardian!")
                    if element == "P":
                        nb_of_pipe += 1
                        if nb_of_pipe > 1:
                            raise ValueError("Error : you should have just 1 Pipe!")
                    if element == "E":
                        nb_of_ether += 1
                        if nb_of_ether > 1:
                            raise ValueError("Error : you should have just 1 Ether!")
                    if element == "N":
                        nb_of_needle += 1
                        if nb_of_needle > 1:
                            raise ValueError("Error : you should have just 1 Needle!")
    """
    I show my list of lists
    """

    def show_maze(self):
        for line in self.map_structure:
            print(line)

    """
    verify if the move is possible: out of the maze, or, on a wall, or, on a path
    return None if forbidden
    """

    def authorize_position(self, pos_col, pos_line):
        walls = "O"
        line_size = len(self.map_structure[0]) - 1
        column_size = len(self.map_structure) - 1
        if (pos_line > line_size) or (pos_col > column_size):
            return False
        if self.map_structure[pos_col][pos_line] != walls:
            return True
        else:
            return False

    """
   Method to write the character's position and erasing is old one
    """

    def move_player(self, character, x_before, y_before, x, y):
        self.map_structure[x_before][y_before] = "."
        self.map_structure[x][y] = character

    """
    Method which return the position of the character in the maze
    """
    def return_position(self, x, y):
        character = self.map_structure[x][y]
        return character

    """
    Method which put the items in the maze
    """
    def put_item(self, character, x, y):
        if self.map_structure[x][y] == ".":
            self.map_structure[x][y] = character

    """
    Method to erase item after being picked up
    """
    def remove_item(self, x, y):
        self.map_structure[x][y] = "M"

    """
    To find all things from one category like paths or walls
    """

    def find_all(self, character):
        # list of position
        positions = []
        # enumerate returns 2 variables. the first one for the line and second for the column
        for x, line in enumerate(self.map_structure):
            for y, column in enumerate(line):
                if character == column:
                    positions.append((x, y))
        return positions


if __name__ == '__main__':
    maze = Labyrinthe("laby.txt")
    maze.pick_up_from_file()
    walls = maze.find_all("O")
    print(walls)
