# 27-A
# with open('27-A_12479.txt') as f:
#     k, n = map(int, f.readline().split())
#     a = [int(i) for i in f]
#     ans = a[0] + a[7] + k
#     for i in range(len(a)):
#         for j in range(i + k, len(a)):
#             if a[i] + a[j] + (j - i) > ans:
#                 ans = a[i] + a[j] + (j - i)
#     print(ans)
# 27-B
from collections import deque
with open('27-B_12479.txt') as f:
    k, n = map(int, f.readline().split())
    a = [int(i) for i in f]
    b = []
    ans = a[0] + a[k] + k
    for i, x in enumerate(a):
        b.append((x, i))
    b.sort(reverse=True)
    for i in range(10000):
        for j in range(i + 1, 10000):
            if b[j][1] - b[i][1] >= k:
                if b[i][0] + b[j][0] + (b[j][1] - b[i][1]) > ans:
                    ans = b[i][0] + b[j][0] + (b[j][1] - b[i][1])
    print(ans)

