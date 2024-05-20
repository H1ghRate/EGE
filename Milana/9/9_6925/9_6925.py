cnt = 0

with open('./9_6925/9_6925.csv') as f:
    for i in f:
        a = list(map(int, i.split(';')))

        x2 = [i for i in a if a.count(i) == 2]

        x1 = [i for i in a if a.count(i) == 1]

        f1 = len(x2) // 2 == 1 and len(x1) == 4

        s1 = s2 = c1 = c2 = 0

        for i in a:
            if i % 2 != 0:
                s1 += i
                c1 += 1
            else:
                s2 += i
                c2 += 1
        
        sr1, sr2 = s1 / c1 if c1 != 0 else 0, s2 / c2 if c2 != 0 else 0

        f2 = abs(sr2 - sr1) > 50

        if f1 != f2:
            cnt += 1

print(cnt)
