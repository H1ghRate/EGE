def perevod(n: int) -> str:
    n_new = ''

    while n:
        n_new += str(n % 3)

        n //= 3
    
    return n_new[::-1]

s_min = 1000000000

for n in range(1, 10000):
    r = perevod(n)

    if (n % 2) == 0:
        r = '2' + r + str(int(r[-1]))
    else:
        r = perevod(int(r[0]) * 2) + r + '2'

    r = int(r, 3)

    if r > 100 and r < s_min:
        s_min = r

print(s_min)
