def check(n):
    return abs(n) % 100 == 21 and abs(n) in range(10**4, 10**5)


a = [int(i) for i in open('./17/egkr_27_04_24/egkr_27_04_24.txt')]

max_elem = max(i for i in a if check(i))
max_elem *= max_elem

cnt = 0
max_sum = 0

for x, y in zip(a, a[1:]):
    f1 = check(x) != check(y)

    f2 = (x * x + y * y) >= max_elem
    
    if f1 and f2:
        cnt += 1
        max_sum = max(max_sum, x + y)

print(cnt, max_sum)
