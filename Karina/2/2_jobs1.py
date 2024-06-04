from itertools import product

print('a b c d')

for a, b, c, d in product(range(2), repeat=4):
    if ((a or b) and (not b == c) and (d or not a)) == False:
        print(a, b, c, d)
