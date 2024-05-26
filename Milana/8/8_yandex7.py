from itertools import product as pr

cnt = 0

for i in pr('ВОЗДУХ', repeat=5):
    i = ''.join(i)

    if (i.count('О') + i.count('У')) == 1:
        i = i.replace('Х', 'В')

        if all(j not in i for j in ['ОВ', 'ВО', 'УВ', 'ВУ']):
            cnt += 1
    
    
print(cnt)
