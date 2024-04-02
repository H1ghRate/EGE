from itertools import product as pr

print('x y z w')

for x, y, z, w in pr(range(2), repeat=4):
    f = (x or (not(y))) and (not(x == z)) and w
    if f:
        print(x, y, z, w)

# z y x w
# 1 0 0 1
# 0 0 1 1
# 0 1 1 1