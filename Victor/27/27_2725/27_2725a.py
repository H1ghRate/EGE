with open('./27_2725/27B_2725.txt') as f:
    n = int(f.readline())

    a = [int(i) for i in f]

cnt = 0

for i in range(n):
    for j in range(i + 1, n):
        if (a[i] - a[j]) % 69 == 0:
            cnt += 1

print(cnt)
# 61