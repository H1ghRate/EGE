arr = [int(i) for i in open('./17_11949/17_11949.txt')]

max_good_elem = max(i for i in arr if abs(i) % 100 == 68)

cnt = 0
max_sum_quad = -100_000 * 4 - 1

for xs in zip(arr, arr[1:], arr[2:], arr[3:]):
    f1 = sum(1 for i in xs if abs(i) in range(10, 100))

    f2 = sum(xs) >= max_good_elem

    if (f1 == 1 or f1 == 4) and f2:
        cnt += 1
        max_sum_quad = max(max_sum_quad, sum(xs))

print(f"Counter: {cnt}.\nMaximum summa of quad: {max_sum_quad}.")
