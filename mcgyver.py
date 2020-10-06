
from minimaze.maze import labyrinthe
from minimaze.maze import view

class McGyver:

    # Initialisation of Mc Gyver and his move in the maze
    def __init__(self):
        self.pos_player = ("x", "y")
        self.pos_line = "x"
        self.pos_col = "y"
        self.sprite = "M"
        self.paths = "."
        self.walls = "O"
        self.depart = "D"
        self.goal = "G"
        self.file = labyrinthe.Labyrinthe.show_list()

    # Display McGyver's face
    def pic_from_hero(self):
        return self.sprite

    def autorize_move(self,pos_col, pos_line):
        """
        verify if the move is possible: out of the maze or on a wall or on a path
        return None if forbidden
        """
        self.n_cols = len(self.file[0])
        self.n_line = len(self.file)
        if pos_line > (self.n_line -1) or pos_col > (self.n_cols - 1):
            return None
        elif self.pos_player == self.walls:
            return None
        else:
            return [self.pos_col, self.pos_line]

    def to_move(self):
        """
        Due to the view.choice, define the position of McGyver in the maze
        :return:
        """
        self.select = view.View.choice
        if self.select == "up":
            move = McGyver.autorize_move(self.file, "x", "y + 1")
        if self.select == "down":
            move = McGyver.autorize_move(self.file, "x", "y - 1")
        if self.select == "left":
            move = McGyver.autorize_move(self.file, "x - 1", "y")
        if self.select == "right":
            move = McGyver.autorize_move(self.file, "x + 1", "y")
        if self.select == "Q":
           quit(labyrinthe)
        # if move == to none print "impossible"






