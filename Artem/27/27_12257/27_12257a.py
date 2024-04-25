with open('./27/27_12257/27A_12257.txt') as f:
    n = int(f.readline())

    a = [int(i) for i in f]

max_len = 1

for i in range(n):
    s = a[i]

    for j in range(i + 1, n):
        s += a[j]

        if s % 113 == 0:
            max_len = max(max_len, j - i + 1)

print(max_len)
