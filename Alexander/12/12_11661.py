for n in range(299, 209, -1):
    s = '3' + '7' * n

    while '27' in s or '377' in s or '777' in s:
        if '27' in s:
            s = s.replace('27', '32', 1)

        if '377' in s:
            s = s.replace('377', '27', 1)
        
        if '777' in s:
            s = s.replace('777', '3', 1)

    if sum(map(int, s)) % 15 == 0:
        print(n)

        break
