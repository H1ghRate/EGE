lst = [int(i) for i in open('./17/10100/17_10100.txt')]

max_good_elem = max(i for i in lst if i % 100 == 13)

cnt = 0
max_summa = -1

for nums in zip(lst, lst[1:], lst[2:]):
    summa = sum(nums)
    f1 = sum(1 for i in nums if 100 <= i <= 999) == 2
    f2 = summa <= max_good_elem
    if f1 and f2:
        cnt += 1
        max_summa = max(max_summa, summa)

print("Counter:", cnt, "\nMaximal summa:", max_summa)
