with open('./27/27_11244/27_A_11244.txt') as f:
    k = int(f.readline())

    n = int(f.readline())

    a = [int(i) for i in f]

max_product = float('-inf')

for i in range(n):
    for j in range(n):
        if i != j:
            if abs(i - j) % k == 0 and max_product < (a[i] * a[j]):
                max_product = a[i] * a[j]

print(max_product)
