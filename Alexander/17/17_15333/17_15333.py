a = [int(i) for i in open('./17_15333/17_15333.txt')]

max_el = max(i for i in a if i % 19 == 0)

cnt = 0
max_sum = 0

for x in zip(a, a[1:]):
    cnd1 = any(i > max_el for i in x)

    if cnd1:
        cnt += 1

        max_sum = max(max_sum, sum(x))
    
print(cnt, max_sum)