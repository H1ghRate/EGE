a = set(range(1, 10000))

def f(x0):
    P = x0 in {2, 4 , 6, 8, 10, 12, 14, 16, 18, 20}
    Q = x0 in {5, 10, 15, 20, 25, 30, 35, 40, 45, 50}
    A = x0 in a

    return (((x0 in A) <= (x0 in P)) and ((x0 in Q) <= (not(x0 in A))))
for x0 in range(1, 10000):
    if f(x0) == 0:
        a.remove(x0)
print(a)