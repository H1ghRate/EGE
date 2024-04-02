idx = 0

with open('./9/9_11658/9_11658.csv') as f:
    for i, line in enumerate(f, 1):
        line = list(map(int, line.split(';')))

        x3 = [i for i in line if line.count(i) == 3]

        x1 = [i for i in line if line.count(i) == 1]

        if len(x3) // 3 == 1 and len(x1) == 4:
            if x3[0] > (sum(line) / len(line)):
                idx = i

print(idx)
