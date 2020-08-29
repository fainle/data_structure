from utils.stack_use_list import Stack


def decimal_to_binary(number: int) -> str:
    s = Stack()
    while number > 0:
        i = number % 2
        s.push(i)
        number //= number

    res_str = ''
    while not s.is_empty():
        res_str += str(s.pop())

    return res_str


assert decimal_to_binary(0) == '0'
assert decimal_to_binary(1) == '01'
assert decimal_to_binary(2) == '10'
assert decimal_to_binary(3) == '11'
assert decimal_to_binary(4) == '100'

