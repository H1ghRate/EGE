from collections import deque

with open('./27/27_9078/27B_9078.txt') as f:
    n, d, t = map(int, f.readline().split())

    a = deque()

    max_x = 0

    max_sum = 0

    c_t = 0

    for _ in range(n):
        x = int(f.readline())
        
        max_x = max(max_x, x)

        if x % d == 0:
            a.append(max_x)
            max_x = 0
            c_t += 1

        if c_t == (t + 2):
            max_sum = max(a[0] + a[t], max_sum)
            a.popleft()
            c_t -= 1

    print(max_sum)
            