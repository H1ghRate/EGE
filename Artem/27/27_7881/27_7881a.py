with open('./27/27_7881/27A_7881.txt') as f:
    n = int(f.readline())

    k = int(f.readline())

    a = [int(i) for i in f]

cnt = 0

for i in range(n):
    for j in range(i + 1, n):
        if j <= i + k:
            if abs(a[i] - a[j]) % 100 == 0 and ((a[i] % 37 == 0) != (a[j] % 37 == 0)):
                cnt += 1

print(cnt)
