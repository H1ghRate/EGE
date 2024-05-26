with open('./27_13942/27B_13942.txt') as f:
    n = int(f.readline())

    a = [int(i) for i in f]

l_max = s = 0

p = {0: 0}

for i in range(n):
    s += a[i]

    if s == 0:
        l_max = max(l_max, i + 1)
    elif s in p:
        l_max = max(l_max, i + 1 - p[s])
    else: 
        p[s] = i + 1

print(l_max)
