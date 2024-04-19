def gcd(a, b):
    if b > a:
        a, b = b, a
    
    return a if b == 0 else gcd(b, a % b)

cnt = 0



for a in range(1, 1000 + 1):
    b = True

    for x in range(1, 1000 + 1):
        if not ((gcd(a, 420) == 2) or ((not(gcd(a, x) == 12)) <= (not(gcd(110, x) == 11)))):
            b = False
            
            break
    
    cnt += b

print(cnt)
