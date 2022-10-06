#Rafael dos Santos Parisi
#RA: 148418


class Stack:
    def __init__(self):
        self.stack = []

    def push(self, int):
        self.stack.append(int)

    def pop(self):
        return self.stack.pop(len(self.stack) - 1)
        