with open('./27/27_12257/27A_12257.txt') as f:
    n = int(f.readline())

    a = [int(i) for i in f]

s_max = 0
len_max = 1

for i in range(n):
    s = a[i]

    if s % 113 == 0 and s > s_max:
        s_max = s
        len_max = 1

    for j in range(i + 1, n):
        s += a[j]

        if s % 113 == 0 and s > s_max:
            s_max = s
            len_max = j - i + 1
        elif s % 113 == 0 and s == s_max:
            len_max = max(len_max, j - i + 1)

print(len_max)
