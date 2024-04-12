from functools import reduce

a = [int(i) for i in open('./17_11236/17_11236.txt')]

min_good_elem = min(i for i in a if i in range(10, 100))

min_good_elem *= min_good_elem

max_good_elem = max(i for i in a if i in range(10 ** 3, 10 ** 4) and abs(i) % 10 == 1)

cnt = 0
max_abs_summa = -1

for xs in zip(a, a[1:], a[2:]):
    f1 = sum(1 for i in xs if i > min_good_elem) == 2

    f2 = reduce(lambda res, curr: abs(res) * abs(curr), xs) % max_good_elem == 0

    if f1 and f2:
        cnt += 1
        max_abs_summa = max(max_abs_summa, reduce(lambda res, curr: abs(res) + abs(curr), xs))
    
print("Counter:", cnt, "\nMaximum abs summa:", max_abs_summa)
