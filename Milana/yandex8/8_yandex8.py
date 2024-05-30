from itertools import product

cnt = 0

for i in product("БАНДЕРОЛЬ", repeat=7):
    s = ''.join(i)

    if s.count('Ь') <= 1:
        for ch in 'БНДРЛ':
            s = s.replace(ch, '*')
        
        if '*Е' not in s and 'Е*' not in s:
            cnt += 1

print(cnt)
