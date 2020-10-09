class Deque:
    """
    双端队列
    """

    def __init__(self):
        """
        初始化
        """
        self.data = []
        self.length = 0

    def add_front(self, item):
        self.length += 1
        self.data.insert(0, item)

    def add_rear(self, item):
        self.length += 1
        self.data.append(item)

    def remove_front(self):
        if self.is_empty():
            return None

        self.length -= 1
        return self.data.pop(0)

    def remove_rear(self):
        if self.is_empty():
            return None

        self.length -= 1
        return self.data.pop()

    def is_empty(self):
        return self.data == []

    def size(self):
        return self.length


if __name__ == '__main__':
    deque = Deque()
    assert deque.is_empty() is True

    deque.add_front(0)
    deque.add_rear(1)
    deque.add_rear(2)

    assert deque.length == 3
    assert deque.remove_front() == 0
    assert deque.remove_rear() == 2
    assert deque.length == 1
    assert deque.remove_front() == 1
    assert deque.length == 0
    assert deque.is_empty() is True
