def f(n):
    b = set()

    for i in range(1, int(n ** 0.5) + 1):
        if n % i == 0:
            b.add(i)
            b.add(n // i)
    
    return sorted(b)

size = 1000000 # 3 8 14 19 28 37 480 960 1920

a = [0] * (size + 1)

b = [0] * (size + 1)

for i in range(1, size + 1):
    a[i] = len(f(i))

b[1] = 0

for i in range(2, size + 1):
    chk = True
    
    for j in range(i - 1, 0, -1):
        if a[i] <= a[j]:
            chk = False
            break
    
    if chk:
        b[i] = 1

last_i = 0

for i in range(size + 1):
    if b[i] == 1:
        print(a[i], ':', b[i])
print("Len: ", sum(1 for i in b if i == 1))