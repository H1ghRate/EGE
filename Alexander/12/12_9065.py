from itertools import product

for n in range(2, 1000):
    if ((4 * n + 43) % n == 0):
        print(n)

