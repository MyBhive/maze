from minimaze.maze import labyrinthe
from minimaze.maze import view
from minimaze.maze import characters
from minimaze.maze import item
from minimaze.maze import character

class Controller(labyrinthe, view, characters, item, character):
#initialisation du personnage
    def __init__(self):
        super(labyrinthe).__init__()
        super(view).__init__()
        super(characters).__init__()
        super(item).__init__()
        super(character).__init__()


    def hero_in_maze(self):

        """Affichage d’un labyrinthe
        lab :Variable contenant le labyrinthe
        perso : caractère représentant le personnage
        pos_perso :liste contenant la position du personnage[ligne, colonne]
        Pas de valeur de retour"""
        n_ligne = 0
        for ligne in self.file:
            if n_ligne == self.pos_player[1]:
            # slicing
                print(ligne[0:self.pos_player[0]] + self.sprite + ligne[self.pos_player[0]+1:])
            else:
                print(ligne)
            n_ligne = n_ligne +1

#collecting items


while True:
    labyrinthe.Labyrinthe.show_list()
    character.McGyver.to_move()

