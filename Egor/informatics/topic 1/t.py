n = int(input())

n = abs(n)

d_1 = n // 1000   
d_2 = n // 100 % 10
d_3 = n // 10 % 10
d_4 = n % 10

print(abs(d_1 - d_4) + abs(d_2 - d_3) + 1)
