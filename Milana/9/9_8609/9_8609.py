c = 0
with open('./9_8609/09_8609.csv') as f:
    for d in f:
        d = sorted(map(int, d.split(';')))

        p = [x for x in d if d.count(x) == 1]

        if len(p) == 5:
            if ((d[0] + d[-1]) * 2) <= (sum(d[1:-1])*3):
                c = c+ 1
print(c)
