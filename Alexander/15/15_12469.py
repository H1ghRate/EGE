from itertools import combinations

def f(x0):
    D = 7 <= x0 <= 68
    C = 29 <= x0 <= 100
    A = st <= x0 <= end

    return D <= (((not(C)) and (not(A))) <= (not(D)))

xs = [x / 4 for x in range(7 * 4, 100 * 4 + 1)]

ans = []

for st, end in combinations(xs, r=2):
    if all(f(x0) == 1 for x0 in xs):
        ans.append(end - st)

print(min(ans))
