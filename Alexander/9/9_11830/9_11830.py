from functools import reduce

cnt = 0

with open('./9/9_11830/9_11830.csv') as f:
    for line in f:
        line = list(map(int, line.split(';')))

        x2 = [i for i in line if line.count(i) == 2]

        x1 = [i for i in line if line.count(i) == 1]

        if len(x2) // 2 == 2 and len(x1) == 3:
            if reduce(lambda res, curr: res * curr, x2) > 2 * reduce(lambda res, curr: res * curr, x1):
                cnt += 1

print(cnt)
