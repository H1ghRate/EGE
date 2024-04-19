N = [0] * 10001

for n in range(4, 1000):
    s = '8' + '4' * n

    while '4444' in s or '844' in s or '84' in s:
        if '4444' in s:
            s = s.replace('4444', '884', 1)

        if '844' in s:
            s = s.replace('844', '488', 1)

        if '84' in s:
            s = s.replace('84', '3343', 1)

    N[n] = len(s)

for n, l in enumerate(N):
    print(n, ':', l)
    input()
