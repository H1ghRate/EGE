def find_divs(n: int) -> set:
    b = set()

    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            b.add(i)
            b.add(n // i)
    
    return sorted(b)

def is_prime(n: int):
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    
    return True

with open('./27_4161/27A_4161.txt') as f:
    n, k = map(int, f.readline().split())

    a = [int(i) for i in f]

l_min = n + 1

for i in range(n):
    l = set(x for x in find_divs(a[i]) if is_prime(x))

    for j in range(i + 1, n):
        l |= set(x for x in find_divs(a[j]) if is_prime(x))

        if len(l) >= k:
            l_min = min(l_min, j - i + 1)

print(l_min)
