from itertools import combinations

def f(x0):
    A = x1 <= x0 <= x2

    B = 24 <= x0 <= 90

    C = 47 <= x0 <= 115

    return C <= (((not(A)) and B) <= (not(C)))

xs = [i / 4 for i in range(23 * 4, 116 * 4 + 1)]

ans = []

for x1, x2 in combinations(xs, 2):
    if all(f(x0) for x0 in xs):
        ans.append(abs(x2 - x1))

print(min(ans))
