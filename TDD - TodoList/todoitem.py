class TodoItem:
    def __init__(self, description):
        self.description = description
        self.isDone = False

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