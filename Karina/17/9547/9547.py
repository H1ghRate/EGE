def three_digit_number(n):
    return 100 <= n <= 999

lst = [int(i) for i in open('./9547/17_9547.txt')]

min_elem = min(i for i in lst if three_digit_number(i) and i % 100 == 11)

cnt = 0
max_sum = 0

for x, y in zip(lst, lst[1:]):
    cnd1 = abs(x - y) % min_elem == 0
    t = abs(x - y)
    cnd2 = sum(1 for i in [x, y] if not three_digit_number(i)) == 1
    
    if cnd1 and cnd2:
        cnt += 1
        max_sum = max(max_sum, x + y)

print(f'Counter: {cnt}\nMaximal summa: {max_sum}')