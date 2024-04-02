cnt = 0

with open('9_12241.csv') as f:
    for line in f:
        line = list(map(int, line.split(';')))
        
        x2 = [x for x in line if line.count(x) == 2]
        
        x1 = [x for x in line if line.count(x) == 1]

        if len(x2) // 2 == 3 and len(x1) == 1:
            if (max(x2) + min(x2)) / 2 < x1[0]:
                cnt += 1

print(cnt)
