import re
from random import choice


class Construction:

    def __init__(self, name_file):
        self.file = name_file
        self.structure = []

    def pick_up_from_file(self):
        with open(self.file, "r") as file:
            for contenu in range(15):
                line = file.readline()
                liste = re.findall("[ot]", line)
                if len(file.readline()) >= 15:
                    liste = liste[:15]
                if len(liste) < 15:
                    liste2 = liste + ["o", "o", "t", "t", "t"] * (3 - len(liste))
                    liste = liste + liste2
                    liste = liste[:15]
                self.structure.append(liste)

    def afficher_liste(self):
        for list in self.structure:
            print(list)


map = Construction("soupe.txt")
map.pick_up_from_file()
map.afficher_liste()