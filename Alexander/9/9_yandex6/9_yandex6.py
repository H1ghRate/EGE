from itertools import permutations as pr

cnt = 0

with open('9_yandex6.csv') as f:
    for line in f:
        a = [int(i) for i in line.split(';')]

        if sum(a) % 2 == 0 and max(a) < (sum(a) - max(a)):
            if any((x + y) == (z + w) for x, y, z, w in pr(a, r=4)):
                cnt += 1

print(cnt)
