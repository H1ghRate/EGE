def perevod(n):
    n_new = ''

    while n:
        n_new += str(n % 3)

        n //= 3
    
    return n_new[::-1]

r_min = 32324234
for n in range(1, 100):
    r = perevod(n)

    r_sum = sum(map(int, r))

    if r_sum % 2 == 0:
        r = '2' + r[2:] + '0'
    else:
        r = '20' + r[2:] + '1'

    r = int(r, 3)

    if r < r_min and r > 75:
        print(n)
        r_min = r