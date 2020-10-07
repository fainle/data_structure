from python.basic.stack_by_list import Stack


def base_conversion(i, to):
    digits = "0123456789ABCDEF"
    s = Stack()

    while i > 0:
        r = i % to
        s.push(r)
        i //= to

    res = ''
    while not s.is_empty():
        res += str(digits[s.pop()])

    return res


if __name__ == '__main__':
    print(base_conversion(100, 2))
    print(base_conversion(100, 8))
    print(base_conversion(100, 10))
    print(base_conversion(100, 16))
    print(base_conversion(10, 16))
