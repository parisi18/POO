from todoitem import TodoItem

class TodoList:
    def __init__(self, owner):
        self.list = []
        self.owner = owner

    def add(self, todoitem):
        self.list.append(todoitem)

    def remove(self, index):
        self.list.pop(index)

    def find(self, description):
        for item in self.list:
            if(item.getDescription() == description):
                return item

    def get(self, index):
        return self.list[index]

    def getOwner(self):
        return self.owner

    def completeItem(self, index):
        self.list[index].complete()
    
    def getListSize(self):
        return len(self.list)