cnt = 0

with open('9_15321.csv') as f:
    for i in f:
        a = list(map(int, i.split(';')))

        a.sort()

        if a[3] < sum(a[:3]):
            if (a[0] + a[3]) == (a[1] + a[2]):
                cnt += 1

print(cnt)
