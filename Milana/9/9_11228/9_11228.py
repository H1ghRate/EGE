summa = 0

with open('9_11228.csv') as f:
    for line in f:
        line = list(map(int, line.split(';')))
        
        x3 = [x for x in line if line.count(x) == 3]

        x2 = [x for x in line if line.count(x) == 2]

        if len(x3) // 3 == 1 and len(x2) // 2 == 2:
            line = sorted(line)

            if sum(x % 2 for x in line[:4]) == 2:
                summa += sum(line)

print(summa)
