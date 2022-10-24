class TodoItem:
    def __init__(self, description, priority):
        self.description = description
        self.isDone = False
        self.priority = priority

    def undo(self):
        self.isDone = False

    def complete(self):
        self.isDone = True
    
    def isDone(self):
        return self.isDone

    def changeDescription(self, description):
        self.description = description

    def getDescription(self):
        return self.description

    def get(self, index):
        return self

    def __lt__(self, other):
        return self.priority.value < other.priority.value

    