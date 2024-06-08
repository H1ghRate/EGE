from fnmatch import fnmatch

def calc_sum_of_digits(n: int) -> int:
    s = 0

    while (n):
        s += n % 10
        n //= 10

    return s

for i in range(86513, 10 ** 12 + 1, 86513):
    if fnmatch(str(i), '17*46??8'):
        sum_of_digits = calc_sum_of_digits(i)

        if int(sum_of_digits ** 0.5) ** 2 == sum_of_digits:
            print(i, i // 86513)