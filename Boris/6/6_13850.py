size = {'a': 3, 'b': 5, 'c': 11}

a = b = c = 0

for _ in range(10):
    a = size['a']

    if (a + b) <= size['b']:
        b += a

        a = 0
    else:
        v = size['b'] - b

        b = size['b'] - b

        a -= v

    if (a + c) <= size['c']:
        c += a

        a = 0
    else:
        v = size['c'] - c

        c = size['c'] - c

        a -= v

    a = size['a']

    if (a + b) <= size['b']:
        b += a

        a = 0
    else:
        v = size['b'] - b

        b += size['b'] - b

        a -= v

    if (a + c) <= size['c']:
        c += a

        a = 0
    else:
        v = size['c'] - c

        c = size['c'] - c

        a -= v

    b = 0

    if (b + c) <= size['b']:
        b += c

        c = 0
    else:
        v = size['b'] - b

        b = size['b'] - b

        c -= v

print(c)
