from itertools import product

cnt = 0

for i in product(range(2), repeat=5):
    if sum(i) % 2 == 0:
        cnt += 1

print(cnt)
