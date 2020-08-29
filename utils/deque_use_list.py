class Deque:
    def __init__(self):
        self._arr = []

    def add_front(self, value):
        self._arr.insert(0, value)
        return

    def add_rear(self, value):
        self._arr.append(value)

    def remove_front(self):
        if self.is_empty():
            return None
        return self._arr.pop(0)

    def remove_rear(self):
        if self.is_empty():
            return None
        return self._arr.pop()

    def is_empty(self):
        return self.size() == 0

    def size(self):
        return len(self._arr)


if __name__ == '__main__':
    d = Deque()
    assert d.remove_rear() is None
    assert d.remove_front() is None
    assert d.is_empty() is True
    d.add_front(2)
    d.add_front(1)
    d.add_rear(3)
    d.add_rear(4)
    assert d.size() == 4
    assert d.remove_front() == 1
    assert d.remove_rear() == 4
    assert d.size() == 2
