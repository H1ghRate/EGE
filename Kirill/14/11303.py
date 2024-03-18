import string

abc = [i for i in '0123456789'] + [i for i in string.ascii_lowercase]

for x in reversed(abc[:20]):
    num1 = int(f'627{x}j8', 20)
    num2 = int(f'h45i{x}5hij', 20)
    num3 = int(f'4idb49j{x}7', 20)
    summa = num1 + num2 + num3
    if (summa % 19) == 0:
        print(summa // 19)
        break