with open('./27/27_7879/27A_7879.txt') as f:
    n = int(f.readline())

    k = int(f.readline())

    a = [int(i) for i in f]

max_sumf = 0

for i in range(n):
    for j in range(i + k, n):
        sumf = a[i] + a[j]

        if sumf % 2023 == 0 and ((a[i] % 47 == 0) != (a[j] % 47 == 0)):
            max_sumf = max(max_sumf, sumf)

print(max_sumf)
