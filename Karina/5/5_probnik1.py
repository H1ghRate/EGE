def perevod(n10):
    n3 = ''
    while n10:
        n3 += str(n10 % 3)
        n10 //= 3

    return n3[::-1]


r_min = 1e16

for n in range(1, 100000):
    r = perevod(n)

    if n % 3 == 0:
        r += r[:2]
    else:
        r += perevod((n % 3) * 5)

    r = int(r, 3)

    if 64 < r < r_min:
        r_min = min(r_min, r)

print(r_min)
