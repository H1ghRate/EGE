# ТРЕХЗНАЧНОЕ

# a = int(input())

# if a < 0:
#     a = -a

# print(a // 100 + a % 10 + (a // 10) % 10)

# ЛЮБОЕ ЧИСЛО ИЗ Z

a = int(input())

if a < 0:
    a = -a

sum_of_digit = 0

while a != 0:
    sum_of_digit += a % 10

    a //= 10

print(sum_of_digit)

# a = input()

# print(sum(map(int, a))) #  a = '232' sum(map(int, a)) -> '2', '3', '2' -> 2, 3, 2 -> 7