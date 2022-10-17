class Basket:
    def __init__(self, l):
        self.location = l
        self.oranges = []

    def add_orange_to_basket(self, o):
        self.oranges.append(o)
