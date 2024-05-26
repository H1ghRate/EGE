def f(n: int) -> list:
    b = set()

    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            if i % 2 == 0:
                b.add(i)
            if (n // i) % 2 == 0:
                b.add(n // i)
    
    return sorted(b)

for i in range(397438, 443520 + 1):
    if len(f(i)) >= 142:
        print(len(f(i)), max(f(i)))

# 143	201600
# 143	205920
# 143	207900
# 143	211680
# 143	214200
# 143	218400
# 167	221760
