cnt = 0

with open('9/9_12241/9_12241.csv') as f:
    for line in f:
        lst = list(map(int, line.split(';')))

        lst2 = [i for i in lst if lst.count(i) == 2]

        lst1 = [i for i in lst if lst.count(i) == 1]

        if len(lst2) == 6 and len(lst1) == 1:
            if (max(lst2) + min(lst2)) // 2 < lst1[0]:
                cnt += 1

print(cnt)
