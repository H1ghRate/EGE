with open('./27_12257/27A_12257.txt') as f:
    n = int(f.readline())

    a = [int(i) for i in f]

max_s = 0
max_len = 0

for i in range(n):
    s = a[i]

    if s % 113 == 0 and s > max_s:
        max_s = s
        max_len = 1
    elif s % 113 == 0 and s == max_s:
        max_len = max(max_len, 1)

    for j in range(i + 1, n):
        s += a[j]

        if s % 113 == 0 and s > max_s:
            max_s = s
            max_len = j - i + 1
        elif s % 113 == 0 and s == max_s:
            max_len = max(max_len, j - i + 1)

print(max_len)
