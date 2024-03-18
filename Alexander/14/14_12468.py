abc = sorted('1234567890qwertyuiopasdfghjklzxcvbnm')[:19]

for x in abc:
    num1 = int(f'78{x}79643', 19)
    num2 = int(f'25{x}43', 19)
    num3 = int(f'63{x}5', 19)

    summa = num1 + num2 + num3

    if summa % 18 == 0:
        print(summa // 18)
        break
