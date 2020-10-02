import re

class Construction:
# init an empty list to make a list of lists later
    def __init__(self, name_file):
        self.file = name_file
        self.structure = []

    def pick_up_from_file(self):
        # I open my file and read it line per line to take out all the "o" and "t" existing inside
        with open(self.file, "r") as file:
            for contenu in range(15):
                line = file.readline()
                liste = re.findall("[ot]", line)
                # if a line is bigger than 15 char, I reduce it to have only 15
                if len(file.readline()) >= 15:
                    liste = liste[:15]
                # if a line as less than 15 char then I had some until I get 15
                if len(liste) < 15:
                    liste2 = liste + ["o"] * (15 - len(liste))
                    liste = liste + liste2
                self.structure.append(liste)

# I know
    def show_list(self):
        for list in self.structure:
            print(list)


map = Construction("soupe.txt")
map.pick_up_from_file()
map.show_list()
