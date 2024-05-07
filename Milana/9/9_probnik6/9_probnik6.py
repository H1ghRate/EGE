cnt = 0

with open('./9/9_probnik6/9_probnik6.csv') as f:
    for ind, line in enumerate(f, 1):
        line = list(map(int, line.split(';')))

        x1 = [i for i in line if line.count(i) == 1]

        xn = [i for i in line if line.count(i) > 1]

        if all((x % 2) != (y % 2) for x, y in zip(line, line[1:])):
            s = 0
            pr = 1

            for x in x1:
                s += x
            
            if len(xn) != 0:
                for x in xn:
                    pr *= x
            else:
                pr = 0
            
            if 3 * s >= pr:
                cnt += ind

print(cnt)
