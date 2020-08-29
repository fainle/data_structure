from utils.stack_use_list import Stack
from string import digits, ascii_lowercase


def infix_to_postfix(string: str) -> str:
    p = {
        '*': 3,
        '/': 3,
        '+': 2,
        '-': 2,
        '(': 1,
    }

    s = Stack()

    res_list = []
    for i in string:
        if i in digits + ascii_lowercase:
            res_list.append(i)
        elif i == '(':
            s.push(i)
        elif i == ')':
            # 结束其中一个表达式
            while not s.is_empty():
                if s.front() != '(':
                    res_list.append(s.pop())
                else:
                    s.pop()
        else:
            # 对比符号 如果符号优先级高则交换
            while not s.is_empty() and p[s.front()] > p[i]:
                res_list.append(s.pop())

            s.push(i)

    while not s.is_empty():
        res_list.append(s.pop())

    return ''.join(res_list)


def postfix_eval(string: str) -> None:
    s = Stack()

    math = {
        '+': lambda a, b: int(a) + int(b),
        '-': lambda a, b: int(a) - int(b),
        '*': lambda a, b: int(a) * int(b),
        '/': lambda a, b: int(int(a) / int(b)),
    }

    for i in string:
        if i in digits:
            s.push(i)
        else:
            b = s.pop()
            a = s.pop()
            do_math = math[i](a, b)
            s.push(do_math)

    return s.pop()


assert infix_to_postfix('(a+b)*c') == 'ab+c*'
assert infix_to_postfix('a+b*c') == 'abc*+'
assert infix_to_postfix('(a+b)*(c+d)') == 'ab+cd+*'
assert infix_to_postfix('(a+b)*d-(d-e)*(f+g)') == 'ab+d*de--fg+*'

assert postfix_eval('22+3*') == 12
assert postfix_eval('223+*') == 10
