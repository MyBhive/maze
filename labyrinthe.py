
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
    I show my list of lists
    """

    def show_list(self):
        for line in self.map_structure:
            print(line)

    """
    To verify that the data in my export file are correct
    """

    def analyze_file(self):
        nb_of_mcgyver = 0
        nb_of_guardian = 0
        for index_line, line in enumerate(self.map_structure):
            for index_element, element in enumerate(line):
                if element not in ["M", "G", "O", "."]:
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

    """
    verify if the move is possible: out of the maze, or, on a wall, or, on a path
    return None if forbidden
    """

    def autorize_move(self, pos_col, pos_line):
        n_col = len(self.map_structure[0])
        n_line = len(self.map_structure)
        paths = "."
        if self.map_structure[pos_line][pos_col] != paths:
            return False
        else:
            return True

    """
       To define the movement of mcgyver
    """
    def move_mcgyver(self, up, down, left, right):
        pos_x = 0
        pos_y = 0
        if up:
            pos_x -= 1
            return pos_x, pos_y
        elif down:
            pos_x += 1
            return pos_x, pos_y
        if left:
            pos_y -= 1
            return pos_x, pos_y
        elif right:
            pos_y += 1
            return pos_x, pos_y
        else:
            return False

    """
    Method to find a character's position.
    """

    def find_one_character(self, character):
        x_character = int()
        y_character = int()
        for x, line in enumerate(self.map_structure):
            for y, column in enumerate(line):
                if character == column:
                    x_character = int(x)
                    y_character = int(y)
        # return the position of this character
        return x_character, y_character

    """
    Method to attribute the position line x and position column y to the character
    """

    def pos_character(self, character, x, y):
        self.map_structure[x][y] = character

    """
    Method which return the position of the character in the maze
    """
    def return_position(self, x, y):
        character = self.map_structure[x][y]
        return character

    """
    To create a list of position to set items in the maze
    """
    def find_all(self, character):
        # lis of position
        positions = []
        # enumerate returns 2 variables. the first one for the line and second for the column
        for x, line in enumerate(self.map_structure):
            for y, column in enumerate(line):
                if character == column:
                    positions.append((x, y))
        return positions


if __name__ == '__main__':
    lab = Labyrinthe('laby.txt')
    (lab.pick_up_from_file())
    print(lab.find_all("."))
