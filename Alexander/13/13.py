from itertools import product

cnt = 0

for s in product([0, 1], repeat=8):
    if s.count(0) <= 2:
        cnt += 1

print(cnt)
