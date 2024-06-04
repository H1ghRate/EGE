from itertools import product

cnt = 0

for line in product(range(5), repeat=7):
    if all(line.count(color) <= 3 for color in range(5)):
        if all(col1 != col2 for col1, col2 in zip(line, line[1:])):
            cnt += 1

print(cnt)
