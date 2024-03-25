with open('input.txt') as f:
    n, k = map(int, f.readline().split())

    a = [int(i) for i in f]

    a.sort()

    a = a[:k]

    a.sort(key=lambda x: x % 2)

    idx = 0

    for i in range(n - 1):
        if a[i] % 2 != a[i + 1] % 2:
            idx = i + 1
            break
     
    print(idx + 1, sum(a[idx:k - 1]))
            