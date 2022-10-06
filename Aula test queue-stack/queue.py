#Rafael dos Santos Parisi
#RA: 148418

class Queue:
    def __init__(self):
        self.queue = []
        pass

    def enqueue(self, int) :
        self.queue.append(int)
        pass

    def dequeue(self):
        return self.queue.pop(0)
