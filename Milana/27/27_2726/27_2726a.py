with open("./27/27_2726/27A_2726.txt") as f:
    n = int(f.readline())

    a = [int(i) for i in f]

max_s = 0

for i in range(n):
    for j in range(i + 1, n):
        if (a[i] + a[j]) % 2 != 0:
            max_s = max(max_s, a[i] + a[j])

print(max_s)