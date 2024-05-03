from functools import lru_cache


@lru_cache(None)
def f(n):
    if n <= 3:
        return 2025

    return 3 * (n - 1) * f(n - 2)


for i in range(1, 2020):
    f(i)

print(f(2027)//f(2023))
