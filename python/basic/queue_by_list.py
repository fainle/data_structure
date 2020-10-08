class Queue:
    def __init__(self):
        self.data = []
        self.length = 0

    def enqueue(self, item):
        """
        插入一个元素到头部 O(n)复杂度
        :param item:
        :return:
        """
        self.data.insert(0, item)
        self.length += 1

    def dequeue(self):
        """
        弹出一个元素 O(1)复杂度
        :return:
        """
        self.length -= 1
        return self.data.pop()

    def is_empty(self):
        return self.data == []

    def size(self):
        return self.length


if __name__ == '__main__':
    queue = Queue()
    assert queue.is_empty() is True
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)
    assert queue.size() == 3
    assert queue.dequeue() == 1
    assert queue.dequeue() == 2
    assert queue.dequeue() == 3
    assert queue.size() == 0
    assert queue.is_empty() is True
