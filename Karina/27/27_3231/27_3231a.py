def find_dist(i, j):
    return min(abs(i - j), n - abs(i - j))

with open('./27/27_3231/27-A_3231.txt') as f:
    n = int(f.readline())

    a = [int(i) for i in f]

min_summa = float('inf')

idx = 0

for i in range(n):
    summa = 0

    for j in range(n):
        summa += find_dist(i, j) * a[j]

    if min_summa > summa:
        min_summa = summa
        idx = i

print(idx + 1)
