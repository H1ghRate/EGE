with open('./27/27_11485/27-A_11485.txt') as f:
    n = int(f.readline())

    a = [int(f.readline()) for _ in range(n)]

    b = [int(f.readline()) for _ in range(n)]

    min_raznost = float('inf')

    for i in a:
        for j in b:
            min_raznost = min(min_raznost, abs(i - j))
    
    print(min_raznost)
