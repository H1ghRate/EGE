lst = [int(i) for i in open('17_13088.txt')]

max_good_element = max(i for i in lst if i % 100 == 17)

cnt = 0

max_summa = -1

for x in zip(lst, lst[1:], lst[2:]):
    f1 = sum(1 for i in x if 1000 <= i <= 9999) == 2
    
    f2 = any(i % 5 == 0 for i in x)
    
    f3 = sum(x) > max_good_element
    
    if f1 and f2 and f3:
        cnt += 1
        max_summa = max(max_summa, sum(x))

print('Counter:', cnt, '\nMaximal summa:', max_summa)
