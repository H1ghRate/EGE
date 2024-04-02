ABC = sorted('1234567890QWERTYUIOPASDFGHJKLZXCVBNM')

def f(x_10: int, base: int) -> str:
    x_n = ''
    while x_10 != 0:
        x_n += ABC[x_10 % base]

        x_10 //= base

    return x_n[::-1]


r_min = 1e10

for n in range(1, 10000):
    r = f(n, 12)

    if n % 4 == 0:
        r = '2' + r + '64'
    else:
        r = r + max(r)
    
    r = int(r, 12)

    if r > 1799 and r < r_min:
        r_min = r

print(r_min)
