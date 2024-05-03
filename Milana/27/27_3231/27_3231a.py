def dist(i, j):
    return min(abs(j - i), n - abs(j - i))


with open('./27/27_3231/27A_3231.txt') as f:
    n = int(f.readline())

    a = [int(i) for i in f]

min_s = n * sum(a)
ind = 0

for i in range(n):
    s = 0

    for j in range(n):
        s += dist(i, j) * a[j]

    if s < min_s:
        min_s = s
        ind = i

print(ind + 1)
