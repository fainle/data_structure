from string import digits, ascii_uppercase


def conversion(num: int, base: int) -> int:
    s = digits + ascii_uppercase

    if num < base:
        return s[num]
    else:
        return conversion(num // base, base) + s[num % base]


if __name__ == '__main__':
    print(conversion(110, 2))
    print(conversion(110, 8))
    print(conversion(110, 16))
    print(conversion(110, 32))
