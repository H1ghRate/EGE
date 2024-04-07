ABC = sorted('123456789qwertyuiopasdfghjklzxcvbnm', reverse=True)

BASE_X = 27

for x in ABC[36-BASE_X:]:
    n1 = int(f'17{x}35', 27)

    n2 = int(f'{x}742M', 27)

    n3 = int(f'{x}', 27) ** 3

    summa = n1 + n2 + n3

    if summa % 23 == 0:
        print(summa // 23)
        break
    