cnt = 0

with open('./9_egkr_27_04_24/9_egkr_27_04_24.csv') as f:
    for i in f:
        a = list(map(int, i.split(';')))

        x3 = [i for i in a if a.count(i) == 3]

        x1 = [i for i in a if a.count(i) == 1]

        if len(x3) == 3 and len(x1) == 4:
            if (sum(x1) / len(x1)) < x3[0]:
                cnt += 1

print(cnt)
