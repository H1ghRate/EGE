def f(x0):
    P = 5 <= x0 <= 54

    Q = 50 <= x0 <= 93

    return ((not(P)) and (Q)) <= (x0 > a)

xs = [x0 for x0 in range(1, 100)]

for a in range(-100, 100):
    if (sum(f(x0) == 0 for x0 in xs)) == 20:
        print(a)
        break
