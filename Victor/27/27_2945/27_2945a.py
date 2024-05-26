with open('./27_2945/27A_2945.txt') as file:
    n = int(file.readline())
    a = [int(i) for i in file]

summa = 0
for i in range(n-1):
    s = a[i]

    if s % 67 == 0:
        summa = max(summa, s)
    for j in range(i+1, n):
        s += a[j]
        if s % 67 == 0:
            summa = max(summa, s)
print(summa)