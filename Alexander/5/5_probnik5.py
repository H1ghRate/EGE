def perevod(n10: int) -> str:
    n3 = ''
    while n10:
        n3 += str(n10 % 3)
        n10 //= 3
    return n3[::-1]

r_min = 1e15

for n in range(1, 1000):
    r = perevod(n)
    if n % 7 == 0:
        r += r[-2:]
    else:
        r += perevod((n % 7) * 3)
    r = int(r, 3)
    if r > 369 and r_min > r:
        r_min = r

print(r_min)
