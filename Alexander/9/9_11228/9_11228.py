summa = 0

with open('./9/9_11228/9_11228.csv') as f:
    for line in f:
        line = list(map(int, line.split(';')))

        x3 = [i for i in line if line.count(i) == 3]

        x2 = [i for i in line if line.count(i) == 2]

        if len(x3) // 3 == 1 and len(x2) // 2 == 2:
            if sum(1 for i in sorted(line)[:4] if i % 2 == 0) == 2:
                summa += sum(line)

print(summa)
