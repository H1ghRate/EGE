from itertools import product as pr

print('x y z w')

for x, y, z, w in pr(range(2), repeat=4):
    f = ((y and (x == (not(z)))) <= w) and (z <= y)
    if not f:
        print(x, y, z, w)

# w z y x
# 0 0 1 1
# 0 1 0 0
# 1 1 0 1