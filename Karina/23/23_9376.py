def f(a: int, b: int, c: bool) -> int:
    if a > b:
        return 0

    if a == b:
        if c:
            return 1
        return 0
    
    c = not c if a == 15 or a == 21 else c

    return f(a + 1, b, c) + f(a + 2, b, c) + f(a * 3, b, c)


print(f(6, 25, False))
