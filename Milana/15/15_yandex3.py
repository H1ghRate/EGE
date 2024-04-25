# from itertools import combinations

# def f(x0):
#     B = 101 <= x0 <= 143
#     C = 144 <= x0 <= 199
#     A = st <= x0 <= end

#     return A <= (B or C)

# xs = [i / 4 for i in range(101 * 4, 199 * 4 + 1)]

# ans = []

# for st, end in combinations(xs, 2):
#     if all(f(x0) for x0 in xs):
#         ans.append(end-st)

# print(max(ans))

from numpy import arange

c = set()
for a1 in arange(100, 200, 0.25):
    for a2 in arange(100, 200, 0.25):
        if all((a1 <= x <= a2) <= ((101 <= x <=143) or (144 <= x <= 199)) for x in arange(100, 200, 0.25)) == 1:
            c.add(a2 - a1)
            
print(max(c))
