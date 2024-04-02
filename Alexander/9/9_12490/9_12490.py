cnt = 0

with open('./9/9_12490/9_12490.csv') as f:
    for line in f:
        line = list(map(int, line.split(';')))

        x2 = [i for i in line if line.count(i) == 2]

        x1 = [i for i in line if line.count(i) == 1]

        if len(x2) // 2 == 1 and len(x1) == 5:
            if line.count(max(line)) == line.count(min(line)):
                cnt += 1

print(cnt)
