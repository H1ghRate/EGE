from functools import lru_cache

@lru_cache(None)
def f(i):
    if i < 10:
        return i
    if i >= 10:
        return g(f(i - 1) % 10) + f(g(i % 10) - 1) - f(i - 3)
    
@lru_cache(None)
def g(i):
    if i < 10:
        return -i
    if i >= 10:
        return f(g(i - 1) % 10) + g(f(i - 1) - 1) + g(i - 2)

for i in range(1110):
    f(i)
    g(i)

print(f(1111) + g(1111))
