with open('./27_14405/27B_14405.txt') as f:
    n, k = map(int, f.readline().split())

    a = [int(i) for i in f]

    osts = [[0] * 7 for _ in range(7)]

    max_elem = 0

    for i in range(n):
        if i > 0:
            osts[0][(a[i] + max_elem) % 7] = a[i] + max_elem if max_elem != 0 else a[i - 7]
            max_elem = max(a[i], max_elem)
        if i > 1 * k:
            osts[1][(a[i] + a[i - 7] + a[i - 14]) % 7] = a[i] + max(osts[0])
        if i > 3 * k:
            osts[2][(a[i] + a[i - 7] + a[i - 14] + a[i - 21]) % 7] = a[i] + max(osts[1])
        if i > 4 * k:
            osts[3][(a[i] + a[i - 7] + a[i - 14] + a[i - 21] + a[i - 28]) % 7] = a[i] + max(osts[2])
        if i > 5 * k:
            osts[4][(a[i] + a[i - 7] + a[i - 14] + a[i - 21] + a[i - 28] + a[i - 35]) % 7] = a[i] + max(osts[3])
        if i > 6 * k:
            osts[5][(a[i] + a[i - 7] + a[i - 14] + a[i - 21] + a[i - 28] + a[i - 35] + a[i - 42]) % 7] = a[i] + max(osts[4])

print(osts[5][0])

