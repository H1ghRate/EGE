def f(n):
    b = set()

    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            b.add(i)
            b.add(n // i)
    
    return sorted(b)

for i in range(397438, 443520 + 1):
    divs = f(i)

    cnt = max_div = 0
    
    for div in divs:
        if div % 2 == 0:
            cnt += 1
            max_div = max(max_div, div)
        
    if cnt >= 142:
        print(cnt, max_div)
