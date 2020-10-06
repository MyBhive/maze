import re

"""
Creating a Labyrinthe class
"""


class Labyrinthe:

    """
    init an empty list to make a list of lists later
    """

    def __init__(self, name_file):
        self.structure = []
        self.file = name_file

    def pick_up_from_file(self):

        # I open my file and read it line per line to take out all the "o" and "t" existing inside
        with open(self.file, "r") as file:
            for contenu in range(15):
                line = file.readline()
                liste = re.findall("[O.]", line)
                # if my list from my line is bigger than 15 char, I reduce it to have only 15
                if len(line) == 15:
                    liste = liste[:15]
                self.structure.append(liste)

    """
    I show my list of lists
    """

    def show_list(self):
        for liste in self.structure:
            print(liste)


map_lab = Labyrinthe("laby.txt")
map_lab.pick_up_from_file()
map_lab.show_list()
