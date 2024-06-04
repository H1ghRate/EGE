from collections import deque

NEEDED_SUM_OF_DIGITS = 65

def sum_of_digits(x: int) -> int:
    sum_of_digits = 0

    while x:
        sum_of_digits += x % 10

        x //= 10

    return sum_of_digits


def is_unique(n: int) -> bool:
    last_digit = n % 10

    n //= 10

    while n:
        if (n % 10) == last_digit:
            return False
        
        last_digit = (n % 10)
    
        n //= 10

    return True

x_max = 98989895
a = deque([x_max])
last_x = x_max

size = 1

sum_of_digits_last = 0

for x in range(x_max - 1, 10 ** 7 - 1, -1):
    sum_of_digits_x = sum_of_digits(x)

    if (last_x == a[size - 1]):
        sum_of_digits_last = sum_of_digits(a[size - 1])

    cnd1 = (sum_of_digits_x - sum_of_digits_last) == 1 

    cnd2 = is_unique(x)

    if cnd1 and cnd2:
        a.append(x)
        size += 1

    last_x = a[size - 1]

for i in range(len(a)):
    if i == 0:
        print(a[i], 0)
    else:
        print(a[i], a[i - 1] - a[i])

