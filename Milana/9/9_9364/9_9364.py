l = 0
with open('./9_9364/9_9364.csv') as f:
    for h in f:
        h = list(map(int, h.split(';')))

        k2 = [x for x in h if h.count(x) == 2]

        k1 = [x for x in h if h.count(x) == 1]

        c = [x for x in h if x %2 == 0]
        n = [x for x in h if x %2 != 0]

        if (len(k2) == 2 and len(k1) == 3) != ((sum(n)) > (sum(c))):
            l = l + 1
print(l)
