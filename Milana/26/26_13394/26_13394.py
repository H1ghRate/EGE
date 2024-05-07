from math import ceil

with open('./26_13394/26_13394.txt') as f:
    n = int(f.readline())

    a = [int(i) for i in f]

a.sort()

s_bad = s_good = 0

cnt_goods = 0

n_goods = sum(i > 350 for i in a)

for x in a:
    if x > 350 and cnt_goods < (n_goods // 3):
        s_bad += x * 0.25
        cnt_goods += 1
    else:
        s_bad += x

s_bad = ceil(s_bad)

cnt = 0

for x in a:
    if x > 350:
        break

    s_good += x
    cnt += 1

for i in range(cnt, n, 3):
    s_good += ceil(a[i] * 0.25 + a[i + 1] + a[i + 2])

print(s_good, s_bad)
