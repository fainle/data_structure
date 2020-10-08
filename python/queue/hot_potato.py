from python.basic.queue_by_list import Queue


def hot_potato(names: list, num: int) -> str:
    queue = Queue()
    for name in names:
        queue.enqueue(name)

    while queue.size() > 1:
        for _ in range(num):
            queue.enqueue(queue.dequeue())  # 循环一圈

        queue.dequeue()  # kill 最后拿到山芋的人

    return queue.dequeue()


if __name__ == "__main__":
    assert hot_potato(["Bill", "David", "Susan", "Jane", "Kent", "Brad"], 7) == 'Susan'
