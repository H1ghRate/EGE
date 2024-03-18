from functools import lru_cache

@lru_cache(None)
def f(n, x):
    if n >= 3000:
        return n
    else:
        return n + x + f(n + 2, x)

for x in range(-10000, 10000):
    if (f(2984, x) - f(2988, x)) == 5916:
        print(x)
