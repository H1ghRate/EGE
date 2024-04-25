with open('./27/27_7896/27A_7896.txt') as f:
    n = int(f.readline())
    k = int(f.readline())
    r = int(f.readline())

    a = [int(i) for i in f]

cnt = 0

for i in range(n):
    for j in range(n):
        if (i + r) <= j <= (i + k):
            if (a[i] + a[j]) % 100 == 77:
                cnt += 1
        
print(cnt)
