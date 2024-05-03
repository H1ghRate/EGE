from itertools import permutations as pr

cnt = 0

for i in pr(range(8), r=6):
    if i[0] != 0 and 3 not in i and any((x % 2 == 0) and (y % 2 == 0) for x, y in zip(i, i[1:])):
        cnt += 1

print(cnt)
