from python.basic.stack_by_list import Stack


def par_checker(string):
    s = Stack()

    d = {
        '(': ')',
        '[': ']',
        '{': '}',
    }

    for i in string:
        if i in "([{":
            s.push(i)
        else:
            p = s.peek()
            if s.is_empty() or d.get(p) != i:
                return False
            else:
                s.pop()
    return s.is_empty()


if __name__ == '__main__':
    assert par_checker('{{([][])}()}') is True
    assert par_checker('[[{{(())}}]]') is True
    assert par_checker('[][][](){}') is True
    assert par_checker('([)]') is False
    assert par_checker('((()]))') is False
    assert par_checker('[{()]') is False
