with open('./27/27_12257/27B_12257.txt') as f:
    n = int(f.readline())

    a = [int(i) for i in f]
    
ost_min = 113 * [n]

ost_max = 113 * [-1]

s = 0

for i in range(n):
    ost_min[s % 113] = min(ost_min[s % 113], i)

    ost_max[s % 113] = max(ost_max[s % 113], i)

    s += a[i]

ans = 0

for i in range(113):
    if ost_min[i] != n and ost_max[i] != -1:
        ans = max(ans, ost_max[i] - ost_min[i])

print(ans)
