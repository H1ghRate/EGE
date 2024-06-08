from itertools import combinations

def f(x0):
    P = 257 <= x0 <= 1000

    Q = 5 <= x0 <= 100

    R = 99 <= x0 <= 258

    A = x1 <= x0 <= x2

    return (A <= R) and ((not(A <= P)) <= Q)


xs = [i/4 for i in range(5 * 4, 1000 * 4 + 1)]

ans = []

for x1, x2 in combinations(xs, 2):
    if (all(x0) for x0 in xs):
        ans.append(abs(x2 - x1))

print(min(ans))
