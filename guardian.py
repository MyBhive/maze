
class McGyver:

    # Initialisation of Mc Gyver and his move in the maze
    def __init__(self):
        self.pos_player = ("x", "y")
        self.sprite = "Gu"

    # Display McGyver's face
    def pic_from_hero(self):
        return self.sprite