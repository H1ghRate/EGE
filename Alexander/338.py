x = int(input())

b = 0

while x != 0:
    b = b * 10 + x % 10
    x //= 10
    
print(b)