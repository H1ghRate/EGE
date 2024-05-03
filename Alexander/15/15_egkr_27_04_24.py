from itertools import combinations

def f(x0):
    P = 24 <= x0 <= 90
    Q = 47 <= x0 <= 115
    A = st <= x0 <= end

    return Q <= ((P and (not(A))) <= (not(Q)))

xs = [x / 4 for x in range(24 * 4, 115 * 4 + 1)]

ans = []

for st, end in combinations(xs, r=2):
    if all(f(x0) for x0 in xs):
        ans.append(end - st)

print(min(ans))
