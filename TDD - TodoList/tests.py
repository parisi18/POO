#Rafael dos Santos Parisi
#148418
#TDD - Assert task status

from operator import truediv
from todoitem import TodoItem
from todolist import TodoList
from user import User

#Assert if task has been done
def test_done():
    item = TodoItem('make bed')
    item.complete()
    assert item.isDone == True

#Assert if task has not been done
def test_undone():
    item = TodoItem('make bed')
    item.complete()
    item.undo()
    assert item.isDone == False

#Assert task description change
def item_change_description():
    item = TodoItem('make bed')
    item.changeDescription(item, 'CHANGE DESCRIPTION')
    assert item.description == 'CHANGE DESCRIPTION'

#Assert getting owner list
def test_owner_todo_list():
    owner = User('Joe Doe', 'joe@doe.com')
    list = TodoList(owner)
    item = TodoItem('make bed')
    list.add(item)
    assert list.get(0) == item
    assert list.getOwner() == owner

#Assert if task has been completed
def test_complete_item_from_todo_list():
    owner = User('Joe Doe', 'joe@doe.com')
    list = TodoList(owner)
    item = TodoItem('make bed')
    list.add(item)
    list.completeItem(0)
    assert item.isDone == True

#Assert removing item from todo list
def test_remove_item_from_todo_list():
    owner = User('Joe Doe', 'joe@doe.com')
    list = TodoList(owner)
    item = TodoItem('make bed')
    list.add(item)
    list.remove(0)
    assert list.getListSize() == 0

#Asserting searching item by description
def test_search_item_by_description():
    owner = User('Joe Doe', 'joe@doe.com')
    list = TodoList(owner)
    item = TodoItem('make bed')
    item2 = TodoItem('withdraw cash')
    list.add(item)
    list.add(item2)
    assert list.find('withdraw cash') == item2
    