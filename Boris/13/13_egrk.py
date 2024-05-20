from itertools import product as pr

cnt = 0

for i in pr(range(2), repeat=15):
    cnt += (i.count(1) + 6) % 11 == 0

print(cnt)
