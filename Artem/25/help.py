from itertools import permutations as pr

for x in pr(range(10), r=8):
    if (x[0] != 0):
        print(x)
        x = sum(x[i] * 10 ** (len(x) - i - 1) for i in range(len(x)))
        print(x)
        input()
