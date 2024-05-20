from itertools import product

cnt = 0

for i in product('01', repeat = 12):
    s = '11001011.01101111.1100' + ''.join(i)

    if s.count('0') % 3 == 0 and  ('000' in s and '111' in s):
        cnt += 1

print(cnt)
