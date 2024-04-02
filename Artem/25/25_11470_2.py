from fnmatch import fnmatch

def f(n):
    b = set()

    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            b.add(i)
            b.add(n // i)
    
    return sorted(b)

for i in range(10**11, 10**10, -60):
    if 240 * 2 ** 4 <= len(f(i)) <= 240 * 2 ** 5:
        print(i)