from itertools import product

cnt = 0

for s in product('01234567', repeat=5):
    s = ''.join(s)

    x3 = [i for i in s if s.count(i) == 3]
    x1 = [i for i in s if s.count(i) == 1]

    if s[0] != '0' and len(x3) // 3 == 1 and len(x1) == 2:
        if ''.join(x3) in s: 
            cnt += 1

print(cnt)
