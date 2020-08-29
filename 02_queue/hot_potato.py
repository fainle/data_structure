from typing import List
from utils.queue_use_list import Queue


def hot_potato(names: List[str], number: int) -> str:
    q = Queue()
    for name in names:
        q.enqueue(name)

    while q.size() > 1:
        for _ in range(number):
            q.enqueue(q.dequeue())

        q.dequeue()

    return q.dequeue()


print(hot_potato(['a', 'b', 'c', 'd', 'e', 'f'], 7))
