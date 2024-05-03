with open("./27/27_2727/27A_2727.txt") as f:
    n = int(f.readline())

    a = [int(i) for i in f]

min_pr = float('inf')

for i in range(n):
    for j in range(i + 1, n):
        if (a[i] * a[j]) % 31 == 0:
            min_pr = min(min_pr, a[i] * a[j])

print(min_pr)
