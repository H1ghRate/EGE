from itertools import product

print('x y z w')

for x, y, z, w in product([0, 1], repeat=4):
    f = (not x and (z <= y) and not w) or ((z == w) and ((x or y) <= w))

    if f:
        print(x, y, z, w)