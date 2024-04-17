# Алгоритм Евклида. (поиск НОД)
# a % b = c1
# b % c1 = c2
# c1 % c2 = c3
# ------------
# НОД: cn-2, когда cn-1 = 0
# Пример:
# 6 % 4 = 2
# 4 % 2 = 0
# НОД: 2, 0 = 0

a, b = int(input()), int(input())

if b > a:
    a, b = b, a

while b != 0:
    a, b = b, a % b

print("НОД:", a)

# print("НОК:", x * y // gcd(x, y))
