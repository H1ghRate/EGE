with open('./27/27_5447/27A_5447.txt') as f:
    n = int(f.readline())

    a = [int(i) for i in f] * 2

s_max = 0

for i in range(n * 2):
    s = a[i]

    for j in range(i + 1, n * 2):
        if (j - i + 1) > n:
            break

        s += a[j]

        if s % 13 == 0 and (j - i + 1) % 13 == 0:
            s_max = max(s_max, s)

print(s_max)
