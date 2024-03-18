from itertools import product as pr

print('x y z w')

for x, y, z, w in pr([0, 1], repeat=4):
    f = ((y and (x == (not z)) <= w)) and (z <= y)
    if not f:
        print(x, y, z, w)
