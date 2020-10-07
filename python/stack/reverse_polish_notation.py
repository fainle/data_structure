from python.basic.stack_by_list import Stack
from string import digits, ascii_lowercase


def infix_to_postfix(string: str) -> str:
    """
    生成后缀表达式
    :param string:
    :return:
    """
    stack = Stack()

    # 运算符优先级
    d = {
        '*': 3,
        '/': 3,
        '+': 2,
        '-': 2,
        '(': 1,
    }

    res = ""
    for s in string:
        # 如果是数字或字母直接加入到表达式里面
        if s in digits + ascii_lowercase:
            res += s
        # 如果是括号则开始压入栈
        elif s == '(':
            stack.push(s)
        # 完成第一个完整到括号表达式
        elif s == ')':
            while not stack.is_empty():
                p = stack.pop()
                if p != '(':
                    res += p
        # 如果是符号则压栈
        else:
            # 对比top的符号如果优先级比当前的大则提前押入栈
            while not stack.is_empty() and d[stack.peek()] > d[s]:
                res += stack.pop()

            stack.push(s)
    # 把栈里面低优先级的全部取出
    while not stack.is_empty():
        res += stack.pop()

    return res


def postfix_eval(string: str) -> None:
    """
    后缀解析
    :param string: 
    :return: 
    """
    stack = Stack()

    math = {
        "+": lambda a, b: int(a) + int(b),
        "-": lambda a, b: int(a) - int(b),
        "*": lambda a, b: int(a) * int(b),
        "/": lambda a, b: int(a) / int(b) if int(b) != 0 else 0,
    }

    for s in string:
        if s not in ['+', '-', '*', '/']:
            stack.push(s)
        else:
            s2 = stack.pop()  # 第二个变量
            s1 = stack.pop()  # 第一个变量
            res = math[s](s1, s2)
            stack.push(res)
    return stack.pop()


if __name__ == '__main__':
    assert infix_to_postfix('(a+b)*c') == 'ab+c*'
    assert infix_to_postfix('a+b*c') == 'abc*+'
    assert infix_to_postfix('(a+b)*(c+d)') == 'ab+cd+*'
    assert infix_to_postfix('(a+b)*d-(d-e)*(f+g)') == 'ab+d*de--fg+*'

    assert postfix_eval('22+3*') == 12
    assert postfix_eval('223+*') == 10
