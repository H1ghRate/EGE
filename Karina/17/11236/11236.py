from functools import reduce


lst = [int(i) for i in open('./17/11236/17_11236.txt')]

min_good_number = min(i for i in lst if 10 <= abs(i) <= 99)
min_good_number *= min_good_number

max_good_number = max(i for i in lst if 1000 <= abs(i) <= 9999 and abs(i) % 10 == 1)

cnt = 0
max_summa = -200_001

for nums in zip(lst, lst[1:], lst[2:]):
    f1 = sum(1 for i in nums if i > min_good_number) == 2
    f2 = reduce(lambda res, current: res * abs(current), nums) % max_good_number == 0
    if f1 and f2:
        cnt += 1
        max_summa = max(max_summa, reduce(lambda res, current: res + abs(current), nums))
    

print("Counter:", cnt, "\nMaximal summa:", max_summa)
