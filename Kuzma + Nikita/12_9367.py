for n in range(1, 100):
    s = 39 * '1' + 40 * '2' + '1' + n * '3'

    while '23' in s or '12' in s or '32' in s:
        if '23' in s:
            s = s.replace('23', '21', 1)
        if '12' in s:
            s = s.replace('12', '1', 1)
        if '32' in s:
            s = s.replace('32', '2', 1)
    
    if sum(map(int, s)) == 100:
        print(n)
        break
