print('x y z w')

for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                f = ((x and not y) <= (z and w)) and ((y <= z) or (w <= x))
                if not f:
                    print(x, y, z, w)

# y z w x
# 0 0 1 1
# 1 0 1 0
# 0 0 0 1