from itertools import combinations

def f(x0):
    P = 13 <= x0 <= 19

    Q = 17 <= x0 <= 23

    A = st <= x0 <= end

    return (not(P or Q)) <= (A <= (Q or P))


xs = [i // 4 for i in range(13 * 4, 23 * 4 + 1)]

ans = []

for st, end in combinations(xs, 2):
    if all(f(x0) for x0 in xs):
        ans.append(end - st)

print(ans)
