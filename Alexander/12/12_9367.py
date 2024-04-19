for n in range(1000):
    s = '2' + '1' * 39 + '3' * n + '2' * 39 + '1'

    while '23' in s or '12' in s or '32' in s:
        if '12' in s:
            s = s.replace('12', '21')

        if '32' in s:
            s = s.replace('32', '1')

        if '23' in s:
            s = s.replace('23', '2')
    
    print(sum(map(int, s)))
    input()

    if sum(map(int, s)) == 100:
        print(n)
        break    
   