# 27-A
# with open('27-A_12257.txt') as f:
#     n = int(f.readline())
#     a = [int(i) for i in f]
#
# k = 113
# s_max, len_max = a[0], 1
# for i in range(n):
#     s = a[i]
#     if s % k == 0:
#         if s > s_max:
#             s_max = s
#             len_max = 1
#     for j in range(i + 1, n):
#         s += a[j]
#         if s % k == 0:
#             cur_len = j - i + 1
#             if s > s_max:
#                 s_max = s
#                 len_max = cur_len
#             elif s == s_max and cur_len > len_max:
#                 len_max = cur_len
# print(len_max)
# 27B
with open('27-A_12257.txt') as f:
    n = int(f.readline())
    a = [int(i) for i in f]
    sums = [[0, 0] for i in range(113)]
    s = 0
    for i in range(n):
        sums[s%113] = sorted(sums[s%113] + [s + a[i]])[1:]
        s += a[i]
    sum_max, len_max = a[0], 1
    for i, vol in enumerate(sums):
        if sum_max > sums[i][1] - sums[i][0]:
            sum_max = sums[i][1] - sums[i][0]
            len_max = 0
        