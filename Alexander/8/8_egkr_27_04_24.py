from itertools import product

cnt = 0

for i in product('0123456', repeat=6):
    s = ''.join(i)

    if s[0] != '0' and s.count('3') == 1:
        for j in '135':
            s = s.replace(j, '*')

        if '**' not in s:
            cnt += 1

print(cnt)
