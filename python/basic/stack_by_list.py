class Stack:
    def __init__(self):
        self.data = []
        self.length = 0

    def push(self, val):
        self.length += 1
        self.data.append(val)

    def pop(self):
        self.length -= 1
        return self.data.pop()

    def peek(self):
        return self.data[self.length - 1]

    def is_empty(self):
        return self.data == []

    def size(self):
        return self.length


if __name__ == '__main__':
    s = Stack()
    assert s.is_empty() is True
    assert s.size() == 0

    s.push(1)
    s.push(2)
    s.push(3)

    assert s.size() == 3
    assert s.peek() == 3
    assert s.pop() == 3

    assert s.length == 2
    s.pop()
    s.pop()

    assert s.is_empty() is True
