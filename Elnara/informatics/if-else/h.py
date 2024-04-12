x_s, y_s = int(input()), int(input())

x_f, y_f = int(input()), int(input())

if abs(x_f - x_s) == abs(y_f - y_s):
    print('YES')
else:
    print('NO')
