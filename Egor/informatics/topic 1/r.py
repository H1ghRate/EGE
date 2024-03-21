n = int(input())

k = int(input())

print(n - (k % n if k % n != 0 else n))
