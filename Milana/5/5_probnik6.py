def f(n10):
    n4 = ''

    while n10:
        n4 += str(n10 % 4)

        n10 //= 4 

    return n4[::-1]



max_r = 0

for n in range(1, 1000):
    r = list(f(n))

    if n % 3 == 0:
        r[0], r[-1] = r[-1], r[0]
        r = ''.join(r)
        r += '1'
    else:
        r = ''.join(r)
        r += str(n % 3)

    r = int(r, 4)

    if r <= 340 and max_r < r:
        max_r = r

print(max_r)
