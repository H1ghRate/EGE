a = [int(i) for i in open('./17_13088/17_13088.txt')]

max_el = max(i for i in a if i % 100 == 17)

cnt = 0
max_sum = 0

for x in zip(a, a[1:], a[2:]):
    cnd1 = sum(1 for i in x if i in range(10 ** 3, 10 ** 4)) == 2

    cnd2 = any(i % 5 == 0 for i in x)

    cnd3 = sum(x) > max_el

    if cnd1 and cnd2 and cnd3:
        cnt += 1

        max_sum = max(max_sum, sum(x))
    
print(cnt, max_sum)
