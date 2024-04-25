with open('./27/27_7876/27A_7876.txt') as f:
    n = int(f.readline())

    k = int(f.readline())

    a = [int(i) for i in f]

cnt = 0

for i in range(n):
    for j in range(i + k, n):
        if (a[i] + a[j]) % 120 == 0 and ((a[i] % 41 == 0) != (a[j] % 41 == 0)):
            cnt += 1

print(cnt)
