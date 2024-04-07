xk, yk = int(input()), int(input())

xf, yf = int(input()), int(input())

f1 = ((yf == (yk + 2)) and ((xf == (xk - 1)) or (xf == (xk + 1))))

f2 = ((yf == (yk - 2)) and ((xf == (xk - 1)) or (xf == (xk + 1))))

f3 = ((xf == (xk + 2)) and ((yf == (yk - 1)) or (yf == (yk + 1))))

f4 = ((xf == (xk - 2)) and ((yf == (yk - 1)) or (yf == (yk + 1))))


if f1 or f2 or f3 or f4:
    print('YES')
else:
    print('NO')
    