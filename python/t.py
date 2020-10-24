a = 15

res = []


def t(a):
    if a % 2 == 0:
        return res.append(a) if a != 0 else res
    else:
        res.append(a - a // 2)
        t(a // 2)


r = t(a)
print(r)
print(res)
