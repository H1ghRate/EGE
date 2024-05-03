from itertools import product

cnt = 0

for n in product(range(7), repeat=6):
    if n[0] != 0 and (sum(1 for i in n if i % 2 == 0)) % 2 == 0 and n.count(0) == 1:
        cnt += 1

print(cnt)
