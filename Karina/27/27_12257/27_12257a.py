with open('./27_12257/27-A_12257.txt') as f:
    n = int(f.readline())

    a = [int(i) for i in f]

max_sum = 0
max_len = 0

K = 113

for i in range(n):
    s = a[i]

    if s % K == 0 and max_sum < s:
        max_sum = s

    for j in range(i + 1, n):
        s += a[j]

        if s % K == 0 and max_sum < s:
            max_sum = s

            max_len = abs(i - j)

print(max_len + 1)
