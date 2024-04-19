from itertools import permutations as pr

cnt = 0

for n in pr(range(10), r=6):
    if n[0] != 0 and n[-1] % 5 == 0:
        if all((x % 2) != (y % 2) for x, y in zip(n, n[1:])):
            cnt += 1

print(cnt)
