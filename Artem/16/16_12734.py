# from functools import lru_cache

# @lru_cache(None)
# def f(n):
#     if n < 52:
#         return n
    
#     return 3 * f(n - 2) - n


# for i in range(50, 15100):
#     f(i)

# print(f(15127) // f(15099))

f = [0] * 16000

for n in range(52):
    f[n] = n

for n in range(52, 16000):
    f[n] = 3 * f[n - 2] - n

print(f[15127] // f[15099])
