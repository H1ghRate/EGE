with open('./27/27_8169/27A_8169.txt') as f:
    k = int(f.readline())
    n = int(f.readline())

    a = [int(i) for i in f]

max_sum = 0

for i in range(n):
    for j in range(i + k, n):
        if abs(a[i] - a[j]) % 2 != 0 and ((a[i] % 26 == 0) != (a[j] % 26 == 0)):
            max_sum = max(max_sum, a[i] + a[j])

print(max_sum)
