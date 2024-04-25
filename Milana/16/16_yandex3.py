from functools import lru_cache

b = set()


@lru_cache(None)
def f(n):
    if n >= 2024:
        return 1
    
    return f(n + 2) + f(n + 4)


for n in range(2024, 0, -1):
    b.add(f(n))

print(len(b))
