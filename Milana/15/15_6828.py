from itertools import combinations

def f(x0):
    P = 257 <= x0 <= 356
    Q = 5 <= x0 <= 600
    R = 59 <= x0 <= 228
    A = a1 <= x0 <= a2

    return ((R) <= (A)) or ((x0 % 3 == 0) <= (P)) <= ((Q) <= (A))

xs = [x0/4 for x0 in range(5 * 4, 600 * 4 + 1)]

a_min = 10000

dlya_x0 = [5, 59, 228, 257, 356, 600]

for i in dlya_x0:
    for j in range(1, 5):
        dlya_x0.append(i + 0.25 * j)

for a1, a2 in combinations(xs, 2):
    if all(f(x0 / 4) for x0 in dlya_x0):
        a_min = min(a_min, a2-a1)
print(a_min)
