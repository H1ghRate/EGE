with open('./26_11940/26_11940.txt') as f:
    n = int(f.readline())

    a = []

    for _ in range(n):
        pos, r = map(int, f.readline().split())

        a.append((pos, r))

a.sort()

m_c = c = 1

b_max = []

for x in range(n):
    x_pos, x_r = a[x]

    b = []

    for y in range(n):
        y_pos, y_r = a[y]

        if x != y and abs(y_pos - x_pos) == y_r + x_r:
            c += 1
            x_pos, x_r = a[y]
            b.append(y_pos + y_r)
    
    if c > m_c:
        m_c = c
        b_max = [i for i in b]

    c = 1
    
print(m_c, max(b_max))