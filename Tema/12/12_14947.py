max_sum_of_digits = 0

for n in range(5000, 6000):
    s = '1' + n * '9'

    while '19' in s or '49' in s or '999' in s:
        if '19' in s:
            s = s.replace('19', '9', 1)
        if '49' in s:
            s = s.replace('49', '91', 1)
        if '999' in s:
            s = s.replace('999', '4', 1)

    max_sum_of_digits = max(max_sum_of_digits, sum(map(int, s)))

print(max_sum_of_digits)
