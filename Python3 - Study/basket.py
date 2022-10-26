class Basket:
    def __init__(self, l):
        self.location = l
        self.oranges = []
        
    def pickOrange(self, o):
        self.oranges.append(o)
