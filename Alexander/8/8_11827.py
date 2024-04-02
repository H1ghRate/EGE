from itertools import product

cnt = 0

for x in product(range(8), repeat=7):
    if x[0] != 0 and sum(1 for i in x if i % 2 == 0) == 2:
        if all((i % 2 == 0 or j != 7) and ((i == 7 and (j % 2 == 0)) or i != 7) for i, j in zip(x, x[1:])):
            cnt += 1

print(cnt)
