def f(a: int, b: int, l_c: str) -> int:
    if a > b:
        return 0

    if a == b:
        return 1
    
    if l_c == 'b':
        return f(a + 2, b, 'a') + f(a * 3, b, 'c')
    
    return f(a + 2, b, 'a') + f(a * a, b, 'b') + f(a * 3, b, 'c')


print(f(2, 64, ''))
