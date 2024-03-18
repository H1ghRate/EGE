def f(a, b):
    if a < b:
        a, b = b, a
    return (a if b == 0 else f(b, a % b))


print(6 * 8 / f(6, 8))
