a = [int(i) for i in open('./17_10719/17_10719.txt')]


cnt = 0
max_summa = -10_000 * 2 - 1

for x, y in zip(a, a[3:]):
    if (abs(x) % 100 == 13) != (abs(y) % 100 == 13):
        cnt += 1
        max_summa = max(max_summa, x + y)
    
print("Counter:", cnt, "\nMaximum summa:", max_summa)
