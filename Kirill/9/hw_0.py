b = set()

for x in range(10, 67):
    for y in range(x):
        num1 = y * 67 ** 0 + 1 * 67 ** 1 + x * 67 ** 2 + 3 * 67 ** 3 + 7 * 67 ** 4
        num2 = 6 * x ** 0 + y * x ** 1 + 9 * x ** 2 + 4 * x ** 3
        summa = num1 + num2
        
        b.add(summa)

print(len(b))
