def is_prime(n):
    if n <= 1:
        return False 

    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    
    return True


a = [int(i) for i in open('./17_9993/17_9993.txt')]

max_elem = max(i for i in a if abs(i) % 100 == 17)

cnt = 0
max_prod = -10**10 - 1

for x, y in zip(a, a[1:]):
    if (is_prime(x) + is_prime(y)) == 1:
        if (x + y) % max_elem == 0:
            cnt += 1
            max_prod = max(max_prod, x * y)

print(cnt, max_prod)
