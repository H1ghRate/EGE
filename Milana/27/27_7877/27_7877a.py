with open('./27/27_7877/27A_7877.txt') as f:
    n = int(f.readline())

    k = int(f.readline())

    a = [int(i) for i in f]

max_sum = 0

for i in range(n):
    for j in range(i + k, n):
        if (a[i] + a[j]) % 101 == 0:
            max_sum = max(max_sum, a[i] + a[j])

print(max_sum)
