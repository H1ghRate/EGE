def perevod(n10: int) -> str:
    n3 = ''
    
    while n10:
        n3 += str(n10 % 3)
        n10 //= 3
        
    return n3[::-1]


r_min = 53495304593405

for n in range(1, 100000):
    r = perevod(n)
    
    if n % 3 == 0:
        r += r[:2]
    else:
        r += perevod((n % 3) * 5)
        
    r = int(r, 3)
    
    if r > 64 and r_min > r:
        r_min = r

print(r_min)