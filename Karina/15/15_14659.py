from itertools import combinations

def f(x0):
    P = 6 <= x0 <= 17

    Q = 13 <= x0 <= 28

    A = x1 <= x0 <= x2

    return (A <= P) or Q


xs = [i/4 for i in range(6 * 4, 28 * 4 + 1)]

ans = []

for x1, x2 in combinations(xs, 2):
    if (all(x0) for x0 in xs):
        ans.append(abs(x2 - x1))

print(max(ans))
