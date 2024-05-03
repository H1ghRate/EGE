from itertools import product as pr

cnt = 0

for i in pr('0123456789ABCDEF', repeat=5):
    s = ''.join(i)

    if s[0] != '0' and s.count('6') == 2:
        for j in '0248ACE':
            s = s.replace(j, '*')
        
        if '*6' not in s and '6*' not in s and '66' not in s:
            cnt += 1

print(cnt)
