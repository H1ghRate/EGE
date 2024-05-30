from itertools import product

print('x y z w')

for x, y, z, w in product(range(2), repeat=4):
    if ((x and y) or ((z == y) and w)) == 0:
        print(x, y, z, w)

