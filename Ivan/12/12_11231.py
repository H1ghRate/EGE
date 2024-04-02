min_summa = 54543954935

for n in range(4, 2_000):
    s = '3' * n + '5'

    while '23' in s or '5333' in s or '33333' in s:
        if '23' in s:
            s = s.replace('23', '3', 1)
        
        if '5333' in s:
            s = s.replace('5333', '32', 1)
             
        if '33333' in s:
            s = s.replace('33333', '55', 1)
    
    summa = sum(map(int, s))

    if summa < min_summa:
        min_summa = summa

print(min_summa)
