with open('example2.txt', 'rt') as f:
    n = int(f.readline())
    a = [[0] * 2 for i in range(2)]
    for _ in range(n):
        x = int(f.readline())
        if x % 2 == 0 and x % 13 == 0:
            a[1][1] += 1
        elif x % 2 == 0 and x % 13 != 0:
            a[1][0] += 1
        elif x % 2 != 0 and x % 13 == 0:
            a[0][1] += 1
        elif x % 2 != 0 and x % 13 != 0:
            a[0][0] += 1
    print(a[0][1] * a[1][0] + a[1][1] * a[0][0] + a[1][1] * a[0][1])
