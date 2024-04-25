with open('./27/27_10727/27A_10727.txt') as f:
    n = int(f.readline())

    a = [int(i) for i in f]

cnt = 0

for i in range(n):
    if a[i] == 0:
        cnt += 1

    for j in range(i + 1, n):
        pos = sum(1 for i in a[i:j + 1] if i > 0)

        neg = sum(1 for i in a[i:j + 1] if i < 0)

        if pos == neg:
            cnt += 1

print(cnt)
