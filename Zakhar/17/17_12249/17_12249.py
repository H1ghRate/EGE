lst = [int(i) for i in open('17_12249.txt')]

max_good_elem = max(i for i in lst if 10000 <= abs(i) <= 99999 and abs(i) % 10 == 3)

cnt = 0

max_summa = -100_000 * 3 - 1

for x in zip(lst, lst[1:], lst[2:]):
    f1 = any(i for i in x if abs(i) % 10 == 3)
    
    f2 = sum(x) <= max_good_elem
    
    if f1 and f2:
        cnt += 1
        
        max_summa = max(max_summa, sum(x))

print('Counter:', cnt, '\nMaximal summa:', max_summa)
