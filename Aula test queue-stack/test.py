#Rafael dos Santos Parisi
#RA: 148418

from queue import Queue
from stack import Stack


def test_stack():
    stack = Stack()
    stack.push(1)
    stack.push(2)
    stack.push(3)

    p = stack.pop()

    assert p == 3

def test_queue():
    queue = Queue()
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)

    d = queue.dequeue()

    assert d == 1