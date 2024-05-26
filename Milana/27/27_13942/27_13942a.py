with open('27A_13942.txt') as file:
    n = int(file.readline())
    a = [int(i) for i in file]

summa = 0
l = 0
for i in range(n-1):
    for j in range(i+1, n):
        summa = sum(a[i:j+1])
        if summa == 0:
            l = max(l, j-i+1)
print(l)