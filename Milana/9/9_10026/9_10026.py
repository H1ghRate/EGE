summa = 0

with open('9_10026.csv') as f:
    i = 0

    for line in f:
        line = list(map(int, line.split(',')))
        i += 1

        if line == sorted(line) or len(set(line)) != len(line):
            summa += i

print(summa)
