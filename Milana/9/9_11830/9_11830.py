cnt = 0

with open('9_11830.csv') as f:
    for line in f:
        line = list(map(int, line.split(';')))

        x2 = [x for x in line if line.count(x) == 2]

        x1 = [x for x in line if line.count(x) == 1]

        if len(x2) // 2 == 2 and len(x1) == 3:
            if x2[0] * x2[1] * x2[2] * x2[3] > 2 * x1[0] * x1[1] * x1[2]:
                cnt += 1

print(cnt)
