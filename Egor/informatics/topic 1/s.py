h = int(input())

a = int(input())
b = int(input())

step = a - b

print((h - a) // step + (((h - a) % step) != 0) + 1)
