s = '1' * 33 + '2' * 33 + '3'

while '11' in s or '22' in s or '13' in s or '23' in s:
    s = s.replace('11', '2')

    s = s.replace('22', '1')

    s = s.replace('13', '2')
    
    s = s.replace('23', '1')

print(s)
