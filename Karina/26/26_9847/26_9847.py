time = [0] * (1440 * 2 + 1)

with open('./26/26_9847/26_9847.txt') as f:
    n = int(f.readline())

    for _ in range(n):
        st, end = map(int, f.readline().split())

        for i in range(st * 2, end * 2):
            time[i] += 1
    
print(*time)
