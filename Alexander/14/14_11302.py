abc = sorted('1234567890qwertyuiopasdfghjklzxcvbnm', reverse=True)[36-25:]

for x in abc:
    num1 = int(f'488926{x}9', 25)
    num2 = int(f'8378{x}2678', 25)
    num3 = int(f'6247{x}9', 25)
    num4 = int(f'4{x}691', 25)
    num5 = int(f'737{x}9{x}89', 25)

    summa = num1 + num2 + num3 + num4 + num5

    if summa % 24 == 0:
        print(summa // 24)
        break
