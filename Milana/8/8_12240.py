from itertools import product

cnt = 0 

for n in product(range(9), repeat=5):
    if n[0] != 0 and n.count(5) == 1 and all(x != y for x, y in zip(n, n[1:])):
        cnt += 1

print(cnt)
