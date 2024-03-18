print('x y z w')
for x in range(0, 2):
    for y in range(0, 2):
        for z in range(0, 2):
            for w in range(0, 2):
                f = (x <= y) and ((not(y)) <= z) and w
                if f:
                    print(x, y, z, w)