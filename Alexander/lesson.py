def f(n):
    if n == 1:
        return 2
    grade, x = 1, 2
    while grade * 2 < n:
        x *= x
        grade *= 2
    if grade == n:
        return x
    else:
        return x * f(n - grade)


print(f(11))
