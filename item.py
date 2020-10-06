
class Items:

    def __init__(self, items):
        self.items = items
        self.position = ("x", "y")

        # random of position in len(file)

    def collecting_items(self):
        if self.items == self.position:
            return True