n = int(input())

m = int(input())

print((((n % m == 0) + (m % n == 0)) == 0) + 1)
