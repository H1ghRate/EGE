cnt = 0

with open('./9/9_12241/9_12241.csv') as f:
    for i in f:
        line = sorted(list(map(int, i.split(';'))))

        x2 = [i for i in line if line.count(i) == 2]

        x1 = [i for i in line if line.count(i) == 1]

        if len(x2) // 2 == 3 and len(x1) == 1:
            if (min(x2) + max(x2)) / 2 < x1[0]:
                cnt += 1

print(cnt)
