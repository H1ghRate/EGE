from functools import lru_cache

b = set()


@lru_cache(None)
def f(a: int, n=0):
    if n > 68:
        return
    if n == 68:
        b.add(a)
    
    f(a + 3, n + 1)
    f(a - 2, n + 1)

f(1)

print(len(b))
