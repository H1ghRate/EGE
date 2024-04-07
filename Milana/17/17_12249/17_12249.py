arr = [int(i) for i in open('./17_12249/17_12249.txt')]

max_good_elem = max(i for i in arr if abs(i) in range(10 ** 4, 10 ** 5) and abs(i) % 10 == 3)

cnt = 0
max_sum_trio = -100_000 * 3 - 1

for xs in zip(arr, arr[1:], arr[2:]):
    f1 = any(abs(i) % 10 == 3 for i in xs)

    f2 = sum(xs) <= max_good_elem

    if f1 and f2:
        cnt += 1
        max_sum_trio = max(max_sum_trio, sum(xs))

print(f"Counter: {cnt}.\nMaximum summa of trios: {max_sum_trio}.")
