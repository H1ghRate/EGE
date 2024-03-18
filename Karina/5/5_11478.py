def perevod(n_10: int) -> str:
    n_6 = ''
    
    while (n_10 != 0):
        n_6 += str(n_10 % 6)
        
        n_10 //= 6
        
    return n_6[::-1]


r_min = 1e15
for n in range(1, 100000):
    r = perevod(n)
    
    if n % 3 == 0:
        r = r + r[:2]
    else:
        r = r + perevod((n % 3) * 10)
    
    if int(r, 6) > 680:
        r_min = min(r_min, int(r, 6))
        
print(r_min)
