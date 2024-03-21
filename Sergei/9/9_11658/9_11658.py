idx = 0

ans = 0

with open('9/9_11658/9_11658.csv') as f:
    for line in f:
        lst = list(map(int, line.split(';')))
        idx += 1

        lst3 = [i for i in lst if lst.count(i) == 3]

        lst1 = [i for i in lst if lst.count(i) == 1]

        if len(lst3) == 3 and len(lst1) == 4:
            if lst3[0] > (sum(lst) / len(lst)):
                ans = idx

print(ans)
