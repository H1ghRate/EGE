from functools import lru_cache

A = lambda x: x + x % 10
B = lambda x: x + x % 68
C = lambda x: x ** 2


@lru_cache(None)
def f(a: int, b:int):
    if a > b or a == 100:
        return 0
    if a == b:
        return 1

    if A(a) != a and B(a) != a and C(a) != a:
        return f(A(a), b) + f(B(a), b) + f(C(a), b)
    if A(a) == a and B(a) != a and C(a) != a:
        return f(B(a), b) + f(C(a), b)
    if A(a) != a and B(a) == a and C(a) != a:
        return f(A(a), b) + f(C(a), b)
    if A(a) != a and B(a) != a and C(a) == a:
        return f(A(a), b) + f(B(a), b)
    if A(a) == a and B(a) == a and C(a) != a:
        return f(C(a), b)
    if A(a) != a and B(a) == a and C(a) == a:
        return f(A(a), b)
    if A(a) == a and B(a) != a and C(a) == a:
        return f(B(a), b)
    
    return 0

print(f(2, 68) * f(68, 680))
 