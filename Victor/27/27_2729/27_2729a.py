with open('./27_2729/27A_2729.txt') as f:
    n = int(f.readline())

    a = [int(i) for i in f]

min_s = max(a) * 3 + 1

for i in range(n):
    for j in range(i + 1, n):
        for k in range(j + 1, n):
            s = a[i] + a[j] + a[k]

            if (s % 11) == 0:
                min_s = min(min_s, s)

print(min_s)
