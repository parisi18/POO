class Barrel:
    def __init__(self, s):
        self.size = s
        self.apples = []

    def add_apple_to_barrel(self, a):
        self.apples.append(a)