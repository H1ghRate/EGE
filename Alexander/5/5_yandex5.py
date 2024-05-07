for n in range(1000, 10000):
    if str(n).count('0') > 0:
        continue

    t = sum(map(int, str(n)))

    ost = [t % int(i) for i in str(n)]

    ost.sort(reverse=True)

    r = int(''.join([str(i) for i in ost]))

    if r > 2000:
        print(n)
        
        break