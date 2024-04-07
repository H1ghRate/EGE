from itertools import product

cnt = 0 

for n in product(range(8), repeat=7):
    if n[0] != 0 and sum(1 for i in n if i % 2 == 0) == 2 and\
          all((x == 7 and y % 2 == 0) or (x != 7 and\
                                           (x % 2 != 0 and y != 7 or x % 2 == 0)) for x, y in zip(n, n[1:])):
        cnt += 1

print(cnt)
