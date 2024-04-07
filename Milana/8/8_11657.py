from itertools import permutations as pr

cnt = 0 

for n in pr(range(8), r=6):
    if n[0] != 0 and 3 not in n and any(x % 2 == 0 and y % 2 == 0 for x, y in zip(n, n[1:])):
        cnt += 1

print(cnt)
