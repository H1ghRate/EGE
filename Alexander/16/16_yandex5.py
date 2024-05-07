from functools import lru_cache

@lru_cache(None)
def f(n):
    if n <= 1:
        return 1
    if n > 1 and n % 2 ==0:
        return f(n - 1)/3
    if n > 1 and n % 2 != 0:
        return 6 * f(n - 1)

cnt = -1
for i in range(1, 2051):
    if i % 2 == 1:
        cnt += 1
    if i % 2 == 0:
        print(cnt, i)