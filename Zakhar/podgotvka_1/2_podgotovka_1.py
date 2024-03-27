from itertools import product as pr

print('x y z w')

for x, y, z, w in pr([0, 1], repeat=4):
    f = (x or y) and not (y == z) and not w
    if f:
        print(x, y, z, w)