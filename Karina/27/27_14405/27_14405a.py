with open('./27_14405/27A_14405.txt') as f:
    n, k = map(int, f.readline().split())

    a = [int(i) for i in f]

    sum_max = 0

    for i1 in range(n):
        for i2 in range(i1 + k, n):
            for i3 in range(i2 + k, n):
                for i4 in range(i3 + k, n):
                    for i5 in range(i4 + k, n):
                        for i6 in range(i5 + k, n):
                            for i7 in range(i6 + k, n):
                                summa = a[i1] + a[i2] + a[i3] + a[i4] + a[i5] + a[i6] + a[i7]

                                if summa % 7 == 0 and summa > sum_max:
                                    sum_max = summa
    
    print(sum_max)
