with open('example1.txt', 'rt') as f:
    n = int(f.readline())
    m_kx = [0] * 10
    for _ in range(n):
        x = int(f.readline())
        m_kx[x % 10] += 1
    s = 0
    for i in range(0, 10):
        for j in range(0, 10):
            if (i * j) % 10 == 3:
                if i == j:
                    s += (m_kx[i] * (m_kx[i] - 1)) // 2
                else:
                    s += m_kx[i] * m_kx[j]
    print(s)
