def gcd(a, b):
    if b > a:
        a, b = b, a
    
    return a if b == 0 else gcd(b, a % b)

# a % b = C1
# b % C1 = C2
# C2 % C1 = C3
# . . .
# Cn-1 % Cn-2 != ... (на нуль делить нельзя)
# Когда Cn-2 = 0 => НОД(a, b) = Сn-1

cnt = 0

for a in range(1, 1000 + 1):
    b = False

    for x in range(1, 1000 + 1):
        b = gcd(a, 420) == 2 or (not(gcd(a, x) == 12)) <= (not(gcd(110, x) == 11))
    
        if not b:
            break

    cnt += b

print(cnt)
