from itertools import permutations as pr

a = 'СОВЕСТЬ'

c = set()

for n in pr(a):
    n = ''.join(n)
    
    s = n
    
    for i in 'СВТ':
        s = s.replace(i, '1')

    for i in 'ОЕЬ':
        s = s.replace(i, '0')
    
    if ('11' in s and '00' in s) == False:
        c.add(n)

print(len(c))
