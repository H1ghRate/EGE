from functools import lru_cache

@lru_cache(None)
def f(n,):
    if n < 10:
        return n
    elif 10 <= n < 1000:
        return f(n // 10) + f(n % 10)
    
    return f(n // 1000) - f(n % 1000)


cnt = 0

for n in range(1000000):
    cnt += f(n) == 0

print(cnt)
