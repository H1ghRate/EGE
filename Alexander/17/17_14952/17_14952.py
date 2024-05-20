a = [int(i) for i in open('./17_14952/17_14952.txt')]

max_el = max(i for i in a if abs(i) % 1000 == 121)

cnt = 0
max_sum = 0

for x in zip(a, a[1:], a[2:]):
    cnd1 = sum(1 for i in x if abs(i) in range(10 ** 3, 10 ** 4) and i % 2 == 0) <= 1

    cnd2 = sum(x) <= max_el

    if cnd1 and cnd2:
        cnt += 1

        max_sum = max(max_sum, sum(x))
    
print(cnt, max_sum)
