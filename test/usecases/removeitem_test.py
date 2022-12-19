from src.usecases.createtodoitem import CreateTodoItem
from src.usecases.createtodolist import CreateTodoList
from src.usecases.removeitem import RemoveItem
from src.usecases.signup import SignUp
from test.usecases.fakehashservice import FakeHashService
from test.usecases.inmemorytodolistrepository import InMemoryTodoListRepository
from test.usecases.inmemoryuserrepository import InMemoryUserRepository


def test_remove_item():
    user_repo = InMemoryUserRepository()
    todolist_repo = InMemoryTodoListRepository()
    hash_service = FakeHashService()
    user_name = 'Joe Doe'
    user_email = 'joe@doe.com'
    user_password = 'test1234TEST&'
    item_description = 'call mom'
    item_priority = 0
    SignUp(user_repo, hash_service).perform(user_name, user_email, user_password)
    CreateTodoList(user_repo, todolist_repo).perform(user_email)
    CreateTodoItem(todolist_repo).perform(user_email, item_description, item_priority)
    usecase = RemoveItem(todolist_repo)
    usecase.perform(user_email, item_description)
    persisted_todolist = todolist_repo.find_by_email(user_email)
    assert persisted_todolist.size() == 0