from python.basic.stack_by_list import Stack


def square(input_string):
    """
    匹配单扣号
    :param input_string:
    :return:
    """
    s = Stack()

    for i in input_string:
        if i == '(':
            s.push(i)
        else:
            if s.is_empty():
                return False
            else:
                s.pop()

    return s.is_empty()


if __name__ == '__main__':
    assert square("(()()()())") is True
    assert square("(((())))") is True
    assert square("(()((())()))") is True
    assert square("((((((())") is False
    assert square("()))") is False
    assert square("(()()(()") is False
