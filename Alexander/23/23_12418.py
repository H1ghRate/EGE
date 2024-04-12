from functools import lru_cache


@lru_cache(None)
def f(a: int, b: int, c_a=0):
    if a > b or a <= 0:
        return 0
    
    if a == b:
        return 1
    
    if c_a == 2:
        return f(a * 2, b, c_a) + f(a * 3, b, c_a)
    
    return f(a - 2, b, c_a + 1) + f(a * 2, b, c_a) + f(a * 3, b, c_a)

print(f(6, 48))