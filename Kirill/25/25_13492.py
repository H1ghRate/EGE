from fnmatch import fnmatch

def f(n: int) -> list:
    b = set()

    b.add(1)

    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            b.add(i)
            b.add(n // i)
    
    return sorted(b)

for i in range(23, 10 ** 6 + 1, 23):
    d_m = max(f(i))

    if fnmatch(str(d_m), '*6215'):
        print(i, d_m) 
