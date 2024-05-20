with open('./27_8513/27A_8513.txt') as f:
    k = int(f.readline())

    n = int(f.readline())

    a = [int(i) for i in f]

max_sum = -1

for i in range(n):
    for j in range(i + k, n):
        max_sum = max(a[i] + a[j], max_sum)

print(max_sum)
