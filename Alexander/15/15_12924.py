a = set(range(1, 10000))

def f(x0):
    P = x0 in {2, 4, 6, 8, 10, 12, 14, 16, 18, 20}
    Q = x0 in {3, 6, 9, 12, 15, 18, 21, 24, 27, 30}
    A = x0 in a
    
    
    return ((A) <= (P)) and ((not(Q)) <= (not(A)))

for x0 in range(1, 10000):
    if f(x0) == 0:
        a.remove(x0)

print(a)
