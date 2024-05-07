from itertools import product

cnt = 0

for i in product(range(2), repeat = 13):
    if 19 == (7 + sum(i)):
        cnt += 1

print(cnt)
