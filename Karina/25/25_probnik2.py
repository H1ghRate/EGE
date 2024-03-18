from fnmatch import fnmatch

def f(n: int) -> bool:
    k0 = k1 = 0
    
    while n:
        if (n % 10) % 2 == 0:
            k0 += 1
        else:
            k1 += 1
        
        n //= 10

    return k0 == k1


for i in range(21025, 10**10 + 1, 21025):
    if fnmatch(str(i), '12*34?5') and f(i):
        print(i, i // 21025)
