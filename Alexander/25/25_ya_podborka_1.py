def f(n: int) -> list:
    b = set()

    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            b.add(i)
            b.add(n // i)
    
    return sorted(b)

pairs = []

for i in range(174457, 174505 + 1):
    devs = f(i)

    if len(devs) == 2:
        pairs.append(devs)

pairs.sort(key=lambda x: x[0] * x[1])

for x, y in pairs:
    print(y)
