lst = [int(i) for i in open('./17/9070/17_9070.txt')]

size = len(lst)

min_good_elem = min(i for i in lst if 100 <= i <= 999 and len(set(str(i))) == 3)

cnt = 0
min_summa = 1e100

for i in range(size // 2):
    f1 = lst[i] * lst[size - i - 1] % min_good_elem == 0
    if f1:
        cnt += 1
        min_summa = min(min_summa, lst[i] + lst[size - i - 1])
    

print("Counter:", cnt, "\nMaximal summa:", min_summa)
