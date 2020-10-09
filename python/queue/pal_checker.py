from python.basic.deque_by_list import Deque


def pal_checker(string: str) -> bool:
    """
    双端队列实现回文字符串检查
    :param string:
    :return:
    """
    deque = Deque()

    for s in string:
        deque.add_rear(s)

    if deque.size() > 1:

        if deque.remove_front() != deque.remove_rear():
            return False

    return True


if __name__ == '__main__':
    assert pal_checker("abc") is False
    assert pal_checker("aba") is True
    assert pal_checker("abba") is True
    assert pal_checker("abcba") is True
    assert pal_checker("abcd") is False
