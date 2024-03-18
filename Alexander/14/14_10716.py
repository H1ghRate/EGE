for x in range(149, -1, -1):
    num1 = 5 * 150 ** 4 + 1 * 150 ** 3 + x * 150 ** 2 + 2 * 150 + 9
    num2 = x * 150 ** 3 + 2 * 150 + 3

    summa = num1 + num2

    if summa % 149 == 0:
        print(summa // 149)
        break
