lst = [int(i) for i in open('17_9164.txt')]

max_good_elem = max(i for i in lst if i % 17 == 0)

cnt = 0
max_sum = -20001

for x, y in zip(lst, lst[1:]):
    sum = x + y
    if sum > max_good_elem:
        cnt += 1
        max_sum = max(max_sum, sum)

print('Counter:', cnt)
print('Maximum summa:', max_sum)
