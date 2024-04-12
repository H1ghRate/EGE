ABC = '1234567890qwertyuiopasdfghjklzxcvbnm'

def perevod(n10: int, base: int) -> str:
    n_base = ''

    while n10 != 0:
        n_base += str(n10 % base)

        n10 //= base
    
    return n_base[::-1]


r_min = 1e20

for n in range(80, 1000):
    r = perevod(n, 8)

    if (r.count('0') + r.count('2') + r.count('4') + r.count('6')) % 2 != 0:
        r = r[-3:] + '46'
    else:
        r = perevod((n % 8) * 5, 8) + r
    
    r = int(r, 8)

    if r < r_min:
        r_min = r

print(r_min)
