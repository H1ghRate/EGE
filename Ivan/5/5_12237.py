r_min = 1e20

for n in range(80, 1000):
    r = oct(n)[2:]

    if (r.count('0') + r.count('2') + r.count('4') + r.count('6')) % 2 != 0:
        r = r[-3:] + '46'
    else:
        r = oct((n % 8) * 5)[2:] + r
    
    r = int(r, 8)

    r_min = min(r_min, r)

print(r_min)
