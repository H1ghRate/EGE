a = [0] * 1000

a[19] = 1

for i in range(19, 10, -1):
    if i - 1 >= 10:
        a[i - 1] += a[i]
    
    if i - 3 >= 10:
        a[i - 3] += a[i]
    
    if i // 2 >= 10:
        a[i // 2] += a[i]

k = a[10]
a[10] = 1

for i in range(10, 3, -1):
    if i == 7:
        continue
 
    a[i - 1] += a[i]

    a[i - 3] += a[i]

    a[i // 2] += a[i]

print(k * a[3])
