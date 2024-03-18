def f(a, b, last_command=''):
    if a > b:
        return 0

    if a == b:
        return 1

    if last_command == 'B':
        return f(a + 2, b, 'A') + f(a * 3, b, 'C')

    return f(a + 2, b, 'A') + f(a ** 2, b, 'B') +\
        f(a * 3, b, 'C')


print(f(2, 64))



# a = [0] * 10000
#
# a[3] = 1
#
# for i in range(3, 20):
#     if i == 16:
#         continue
#     if (i + 1) <= 20:
#         a[i + 1] += a[i]
#     if (i + 3) <= 20:
#         a[i + 3] += a[i]
#     if (i ** 2) <= 20:
#         a[i ** 2] += a[i]
#
# k = a[20]
# a[20] = 1
#
# for i in range(20, 26):
#     a[i + 1] += a[i]
#     a[i + 3] += a[i]
#     a[i ** 2] += a[i]
#
# print(k * a[26])
