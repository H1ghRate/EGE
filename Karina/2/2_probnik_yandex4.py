from itertools import product

print('x y w f')

for x, y, w in product(range(2), repeat=3):
    if (x <= y) and (w or not w):
        print(x, y, w, 1)
    else:
        print(x, y, w, 0)