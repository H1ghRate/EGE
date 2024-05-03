K = 137

with open('./27_egkr_27_04_24/27A_egkr_27_04_24.txt') as f:
    n = int(f.readline())

    a = [int(i) for i in f]

max_s = 0
max_l = 0

for i in range(n):
    s = a[i]

    if s % K == 0 and s > max_s:
        max_s = s
        max_l = 1
    
    for j in range(i + 1, n):
        s += a[j]

        if s % K == 0 and s > max_s:
            max_s = s
            max_l = j - i + 1
        elif s % K == 0 and s == max_s:
            max_l = max(max_l, j - i + 1)

print(max_l)
