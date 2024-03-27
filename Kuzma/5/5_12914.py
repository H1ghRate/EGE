r_max = -1

for n in range(1, 1000):
    r = bin(n)[2:]

    if n % 3 == 0:
        r = r.replace('0', '11')
    else:
        r = r.replace('1', '10')
    
    r = int(r, 2)

    if r <= 161 and r > r_max:
        r_max = r

print(r_max)
