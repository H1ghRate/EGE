def dist(i, j):
    return min(abs(j - i), n - abs(j - i))

with open('./27/27_3231/27A_3231.txt') as f:
    n = int(f.readline())

    a = [int(i) for i in f]

s_min = float('inf')
idx = 0

for i in range(n):
    s = 0
    for j in range(n):
        s += a[j] * dist(i, j)
    
    if s < s_min:
        s_min = s
        idx = i

print(idx + 1)
