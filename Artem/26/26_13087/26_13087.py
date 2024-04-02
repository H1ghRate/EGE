with open('26_13087.txt') as f:
    n = int(f.readline())

    a = []

    for _ in range(n):
        st, end = map(int, f.readline().split())
    
        a.append((st, end))

    a.sort(key=lambda x: x[1])

    prev_last_time = 0
    last_time = 0
    cnt = 0

    for i in a:
        st, end = i
        if st >= last_time:
            prev_last_time = last_time - 20
            last_time = end + 20
            cnt += 1
    
    print(cnt, max(i[0] for i in a) - prev_last_time)
