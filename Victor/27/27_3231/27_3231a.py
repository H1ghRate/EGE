def dist(i, j):
    return min(abs(i - j), n - abs(i - j))


with open('./27/27_3231/27A_3231.txt') as f:
    n = int(f.readline())

    a = [int(i) for i in f]


min_sum = float('inf')
ans = 0

for i in range(n):
    sum = 0
    for j in range(n):
        sum += a[j] * dist(i, j)
    
    if sum < min_sum:
        min_sum = sum
        ans = i + 1

print(ans)
