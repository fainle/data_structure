class Stack:
    def __init__(self):
        self._arr = []

    def push(self, value):
        self._arr.append(value)
        return

    def pop(self):
        return self._arr.pop()

    def front(self):
        return self._arr[self.size() - 1]

    def size(self):
        return len(self._arr)

    def is_empty(self):
        return self._arr == []


if __name__ == '__main__':
    s = Stack()
    assert s.is_empty() is True
    s.push(1)
    s.push(2)
    assert s.front() == 2
    s.push(3)
    assert s.size() == 3
    assert s.pop() == 3
    assert s.size() == 2
