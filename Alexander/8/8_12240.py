from itertools import product as pr

cnt = 0

for i in pr(range(9), repeat=5):
    if i[0] != 0 and i.count(5) == 1 and all(x != y for x, y in zip(i, i[1:])):
        cnt += 1

print(cnt)
