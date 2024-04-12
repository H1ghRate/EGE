a = [int(i) for i in open('./17_11838/17_11838.txt')]

max_good_elem = max(i for i in a if abs(i) % 100 == 50)

cnt = 0
max_summa = -100_000 * 3 - 1

for xs in zip(a, a[1:], a[2:]):
    f1 = len(set(xs)) == 3 and all(abs(i) in range(10 ** 4, 10 ** 5) for i in xs)
    f2 = sum(xs) <= max_good_elem

    if f1 and f2:
        cnt += 1
        max_summa = max(max_summa, sum(xs))

print("Counter:", cnt, "\nMaximum summa:", max_summa)
