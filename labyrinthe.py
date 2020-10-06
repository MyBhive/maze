import re

class Labyrinthe:
# init an empty list to make a list of lists later
    def __init__(self):
        self.structure = []

    def pick_up_from_file(self, name_file):
        self.file = name_file
        # I open my file and read it line per line to take out all the "o" and "t" existing inside
        with open(self.file, "r") as file:
            for contenu in range(15):
                line = file.readline()
                liste = re.findall("[O.]", line)
                # if my list from my line is bigger than 15 char, I reduce it to have only 15
                if len(line) == 15:
                    liste = liste[:15]
                self.structure.append(liste)

# I show my list of lists
    def show_list(self):
        for list in self.structure:
            print(list)


map = Labyrinthe()
map.pick_up_from_file("laby.txt")
map.show_list()