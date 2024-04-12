def f(a: int, b: int):
    if a > b or a == 16:
        return 0
    
    if a == b:
        return 1

    return f(a + 1, b) + f(a + 3, b) + f(a ** 2, b)

print(f(3, 20) * f(20, 26))
