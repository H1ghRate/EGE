for n in range(1000, 0, -1):
    r = bin(n)[2:]

    if sum(map(int, r)) % 2 == 0:
        r = '10' + r[2:] + '0'
    else:
        r = '11' + r[2:] + '1'
    
    if int(r, 2) < 35:
        print(n)
        break