from utils.deque_use_list import Deque


def pal_checker(string: str) -> bool:
    d = Deque()
    for i in string:
        d.add_rear(i)

    while d.size() > 1:
        front = d.remove_front()
        rear = d.remove_rear()
        if front != rear:
            return False

    return True


assert pal_checker('abc') is False
assert pal_checker('abcd') is False
assert pal_checker('cbc') is True
assert pal_checker('abba') is True
assert pal_checker('abcba') is True
