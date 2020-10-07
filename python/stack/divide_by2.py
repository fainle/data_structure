from python.basic.stack_by_list import Stack


def divide_by2(i):
    s = Stack()

    while i != 0:
        r = i % 2
        s.push(r)
        i //= 2

    res = ''
    while not s.is_empty():
        res += str(s.pop())

    return res


if __name__ == '__main__':
    assert divide_by2(5) == '101'
    assert divide_by2(10) == '1010'
