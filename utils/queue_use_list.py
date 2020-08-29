class Queue:
    def __init__(self):
        self._arr = []

    def enqueue(self, value):
        self._arr.insert(0, value)
        return

    def dequeue(self):
        return self._arr.pop()

    def is_empty(self):
        return self.size() == 0

    def size(self):
        return len(self._arr)


if __name__ == '__main__':
    q = Queue()
    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)
    assert q.size() == 3
    assert q.dequeue() == 1
    assert q.dequeue() == 2
    assert q.dequeue() == 3
    assert q.is_empty() is True
    q.enqueue(4)
    assert q.size() == 1
