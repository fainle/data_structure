from utils.stack_use_list import Stack


def base_conversion(number: int, to: int) -> str:
    digits = '0123456789ABCDEF'
    s = Stack()

    while number > 0:
        i = number % to
        s.push(i)
        number //= to

    res_str = ''
    while not s.is_empty():
        res_str += str(digits[s.pop()])

    return res_str


print(base_conversion(100, 2))
print(base_conversion(100, 8))
print(base_conversion(100, 10))
print(base_conversion(100, 16))

