with open('./27_9794/27A_9794.txt') as f:
    k = int(f.readline())

    n = int(f.readline())

    a = [int(i) for i in f]

cnt = 0

for i in range(n):
    for j in range(i + 1, n):
        if (a[i] + a[j]) >= k:
            cnt += 1

print(cnt)
