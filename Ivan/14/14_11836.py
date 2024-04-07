ABC = sorted('1234567890qwertyuiopasdfghjklzxcvbnm')

BASE_X = 32

for x in ABC[:BASE_X]:
    n1 = int(f'931{x}964', 32)

    n2 = int(f'4{x}51{x}1', 32)

    n3 = int(f'2861{x}637', 32)

    summa = n1 + n2 + n3

    if (summa % 31) == 0:
        print(summa // 31)
        break
