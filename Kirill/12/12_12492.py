max_summa = -1

for n in range(4, 10000):
    s = '3' + n * '5'

    while '333' in s or '555' in s:
        if '555' in s:
            s = s.replace('555', '3', 1)
        else:
            s = s.replace('333', '5', 1)

    max_summa = max(max_summa, sum(map(int, s)))

print(max_summa)
