cnt = 0

with open('9/9_7030/9_7030.csv') as f:
    for line in f:
        lst = list(map(int, line.split(';')))

        lst3 = []

        for i in lst:
            if i not in lst3 and lst.count(i) == 2:
                lst3.append(i)
        
        if len(lst3) == 3:
            lst3.sort()

            if (lst3[0] + lst3[1]) > lst3[2] and (lst3[0] ** 2 + lst3[1] ** 2) == lst3[2] ** 2:
                cnt += 1

print(cnt)