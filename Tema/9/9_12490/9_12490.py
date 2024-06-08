cnt = 0

with open('9_12490.csv') as f:
    for i in f:
        a = list(map(int, i.split(';')))

        x2 = [i for i in a if a.count(i) == 2]

        x1 = [i for i in a if a.count(i) == 1]

        if len(x2) // 2 == 1 and len(x1) == 5:
            if (a.count(max(a)) == a.count(min(a))):
                cnt += 1

print(cnt)
