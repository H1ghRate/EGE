def f(a: int, b: int) -> int:
    if a > b or a == 32:
        return 0
    
    if a == b:
        return 1
    
    return f(a + 2, b) + f(a + 4, b)

print(f(9, 27) * f(27, 29) * f(29, 37))
