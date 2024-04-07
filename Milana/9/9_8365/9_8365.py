from itertools import permutations

c = 0
with open('./9_8365/9_8365.csv') as f:
    for h in f:
        h = sorted(map(int, h.split(';')))
        k = [x for x in h if h.count(x) == 1]

        if len(k) == 5:
            if any((hs[0] + hs[1]) / 2 == (sum(h) - sum(hs)) and (hs[2] + hs[3]) / 2 == (sum(h) - sum(hs)) for hs in permutations(h, r=4)):
                c = c + 1
print(c)
