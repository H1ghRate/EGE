def f(x0):
    D = 15 <= x0 <= 40

    C = 21 <= x0 <= 63

    A = 7 <= x0 <= e

    return D <= (((not(C)) and (not(A))) <= (not(D)))

xs = [x0 / 4 for x0 in range(-1000 * 4, 1000 * 4 + 1)]

for e in range(-1000, 1000):
    if all(f(x0) for x0 in xs):
        print(e)
        break
