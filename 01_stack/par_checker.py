from utils.stack_use_list import Stack


def par_checker(string: str) -> bool:
    p = {
        '(': ')',
        '[': ']',
        '{': '}'
    }

    s = Stack()
    for i in string:
        if i in '([{':
            s.push(i)
        elif i in '}])':
            end = s.front()
            if p.get(end) == i:
                s.pop()
            else:
                return False

    return s.is_empty()


assert par_checker('(())(())') is True
assert par_checker('(())(()') is False
assert par_checker('([{}])') is True
assert par_checker('([{}]') is False
assert par_checker('({[}])') is False
