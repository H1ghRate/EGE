lst = [int(i) for i in open('./17/12249/17_12249.txt')]

max_good_elem = max(i for i in lst if 10000<=abs(i)<=99999 and abs(i) % 10 == 3)

cnt = 0
max_sum = -200001

for nums in zip(lst, lst[1:], lst[2:]):
    f1 = any(abs(i) % 10 == 3 for i in nums)
    f2 = sum(nums) <= max_good_elem
    if f1 and f2:
        cnt += 1
        max_sum = max(max_sum, sum(nums))

print("Counter:", cnt, "\nMaximal summa:", max_sum)
