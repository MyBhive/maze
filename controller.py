from minimaze.maze import labyrinthe
from minimaze.maze import view
from minimaze.maze import guardian
from minimaze.maze import item
from minimaze.maze import mcgyver

class Controller(labyrinthe,view,guardian,item,mcgyver):
#initialisation du personnage
    def __init__(self):
        super(labyrinthe).__init__()
        super(view).__init__()
        super(guardian).__init__()
        super(item).__init__()
        super(mcgyver).__init__()


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



while True:
    labyrinthe.Labyrinthe.show_list()
    mcgyver.McGyver.to_move()

