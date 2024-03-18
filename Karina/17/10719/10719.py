lst = [int(i) for i in open('./10719/17_10719.txt')]

n = len(lst)

cnt = 0
max_sum = -20001

for x, y in zip(lst, lst[3:]):
    cnd = (abs(x) % 100 == 13) != (abs(y) % 100 == 13)
    
    if cnd:
        cnt += 1
        max_sum = max(max_sum, x + y)

print('Counter:', cnt)
print('Maximal summa:', max_sum)
