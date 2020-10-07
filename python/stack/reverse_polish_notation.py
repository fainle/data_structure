from python.basic.stack_by_list import Stack
from string import digits, ascii_lowercase


def infix_to_postfix(string: str) -> str:
    stack = Stack()

    res = ""
    for s in string:
        if s in digits + ascii_lowercase:
            res += s

    while not stack.is_empty():
        res += stack.pop()

    print(res)
    return res


if __name__ == '__main__':
    assert infix_to_postfix('(a+b)*c') == 'ab+c*'
    assert infix_to_postfix('a+b*c') == 'abc*+'
    assert infix_to_postfix('(a+b)*(c+d)') == 'ab+cd+*'
    assert infix_to_postfix('(a+b)*d-(d-e)*(f+g)') == 'ab+d*de--fg+*'
