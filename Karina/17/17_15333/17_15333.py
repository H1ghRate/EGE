a = [int(i) for i in open('./17_15333/17_15333.txt')]

max_elem = max(i for i in a if i % 19 == 0)

cnt = 0
max_s = 0

for x, y in zip(a, a[1:]):
    if x > max_elem or y > max_elem:
        cnt += 1
        max_s = max(max_s, x + y)

print(cnt, max_s)