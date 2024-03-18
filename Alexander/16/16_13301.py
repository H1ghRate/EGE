from functools import lru_cache

@lru_cache(None)
def f(n):
    if n == 1:
        return 1
    if n > 1:
        return (4 * n + 7) * f(n - 1) + 16

print(10*12//(10**12 + 1))
