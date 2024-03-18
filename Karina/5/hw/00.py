def perevod(n_10: int, osn: int) -> str:
    abc = sorted('0123456789qwertyuiopasdfghjklzxcvbnm')
    
    n = ''
    
    while (n_10 != 0):
        n += abc[n_10 % osn]
        
        n_10 //= osn
        
    return n[::-1]


r_min = 1e20
for n in range(1000):
    r = perevod(n, 12)
    
    if n % 4 == 0:
        r = '2' + r + '64'
    else:
        r = r + max(r)
    
    r = int(r, 12)
    
    if r > 1799 and r < r_min:
        r_min = r

print('Minimum R:', r_min)
     