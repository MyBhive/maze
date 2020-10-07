from minimaze.maze import labyrinthe
from minimaze.maze import view
from minimaze.maze import characters
from minimaze.maze import item

class Controller(labyrinthe, view, characters, item, characters):
#initialisation du personnage
    def __init__(self):
        super(labyrinthe).__init__()
        super(view).__init__()
        super(characters).__init__()
        super(item).__init__()
        super(characters).__init__()


#collecting items


while True:
    labyrinthe.Labyrinthe.show_list()
    characters.McGyver.to_move()

