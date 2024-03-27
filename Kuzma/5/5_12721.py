def perevod(num10: int, base: int) -> str:
    num_base = ''

    while num10 != 0:
        num_base += str(num10 % base)
        
        num10 //= base
    
    return num_base[::-1]


r_min = float('inf')

for n in range(80, 1000):
    r = perevod(n, 8)

    if sum(r.count(i) for i in '0246') % 2 != 0:
        r = r[-3:] + '46'
    else:
        r = perevod((n % 8) * 5, 8) + r
    
    r = int(r, 8)

    if r < r_min:
        r_min = r

print(r_min)
