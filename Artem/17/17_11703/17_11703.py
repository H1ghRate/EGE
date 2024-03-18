from functools import reduce

lst = [int(i) for i in open('17_11703.txt')]

max_good_elem = max(i for i in lst if abs(i) % 100 == 18)

counter = 0
max_product = -100001

for trio in zip(lst, lst[1:], lst[2:]):
    product = reduce(lambda res, current: current * res, trio)

    f1 = any(10000 <= abs(i) <= 99999 for i in trio)
    f2 = product % max_good_elem == 0

    if f1 and f2:
        counter += 1
        max_product = max(max_product, product)

print('Counter:', counter, '\nMax product:', max_product)