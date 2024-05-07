def dist(i, j):
    return min(abs(j - i), n - abs(j - i))


with open('./27/27_3231/27B_3231.txt') as f:
    n = int(f.readline())

    a = [int(i) for i in f] * 2

pref_a = [0] * (2 * n + 1)

for i in range(2 * n):
    pref_a[i + 1] = pref_a[i] + a[i]

s1 = sum(dist(0, j) * a[j] for j in range(n))

min_s = s1
ind = 0

for i in range(1, n):
    n1 = pref_a[n + i] - pref_a[n // 2 + i]

    n2 = pref_a[n // 2 + i] - pref_a[i]  

    s1 += n1 - n2

    if s1 < min_s:
        min_s = s1
        
        ind = i

print(ind + 1)
