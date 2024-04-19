# f = [0] * 7000

# for n in range(1, 6 + 1):
#     f[n] = n

# for n in range(7, 6200):
#     f[n] = 2 * n + 3 + f[n - 1]

# print(f[6188] - f[6185])

from functools import lru_cache

@lru_cache(None)
def f(n):
    if n <= 6:
        return n
    
    if n > 6:
        return 2 * n + 3 + f(n - 1)
    
for i in range(7, 6100):
    f(i)

print(f(6188) - f(6185))