with open('./27_12257/27-B_12257.txt') as f:
    n = int(f.readline())

    a = [int(i) for i in f]

K = 113

s_max = [(0, 0)] * 113

s_min = [(1e15, 1e15)] * 113

s = 0 

for i in range(n):
    s += a[i]

    s_max[s % K] = sorted([s_max[s % K], (s, i)], reverse = True)[0]

    s_min[s % K] = sorted([s_min[s % K], (s, i)])[0]

l_max = 0

for i in range(K):
    if s_max[i] != 0 and s_min[i] != 1e15:
        l_max = max(s_max[i][1] - s_min[i][1], l_max)

print(l_max)
