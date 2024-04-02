from fnmatch import fnmatch

def f(n):
    b = set()

    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            b.add(i)
            b.add(n // i)
    
    return sorted(b)

for i in range(1, 10**7 + 1):
    if fnmatch(str(i), '3?1111*') and len(f(i)) == 0:
        print(i)
