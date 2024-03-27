def perevod(num10: int, base: int) -> str:
    ABC = sorted('1234567890WERTYUIOPASDFGHJKLZXCVBNM')

    num_base = ''

    while num10 != 0:
        num_base += ABC[num10 % base]
        
        num10 //= base
    
    return num_base[::-1]

def r(n: int) -> int:
    rn = perevod(n, 12)

    if n % 4 == 0:
        rn += '2' + rn + '64'
    else:
        rn += max(rn)

    return int(rn, 12)

is_first = True
r_min = 0

for n in range(2, 10000):
    rn = r(n)

    if rn > 1799 and (rn < r_min or is_first):
        r_min = rn
        is_first = False

print(r_min)
