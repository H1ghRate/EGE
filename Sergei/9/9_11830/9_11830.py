cnt = 0

with open('9/9_11830/9_11830.csv') as f:
    for line in f:
        lst = list(map(int, line.split(';')))

        lst2 = [i for i in lst if lst.count(i) == 2]

        lst1 = [i for i in lst if lst.count(i) == 1]

        if len(lst2) == 4 and len(lst1) == 3:
            pr2 = pr1 = 1

            for i in lst2:
                pr2 *= i
            
            for i in lst1:
                pr1 *= i
            
            if pr2 > (2 * pr1):
                cnt += 1

print(cnt)
