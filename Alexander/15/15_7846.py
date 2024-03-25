from itertools import combinations

def f(x0):
    P = 13 <= x0 <= 19
    Q = 17 <= x0 <= 23
    A = st <= x0 <= end

    return (not ((not(P)) <= Q)) <= (A <= ((not(Q)) <= P))

xs = [x / 4 for x in range(13 * 4, 23 * 4 + 1)]

ans = []

for st, end in combinations(xs, r=2):
    if all(f(x0) == 1 for x0 in xs):
        ans.append(end - st)

print(max(ans))
