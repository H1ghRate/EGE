ABC = sorted('123456789qwertyuiopasdfghjklzxcvbnm')

BASE_X = 13

for x in ABC[:BASE_X]:
    n1 = int(f'9{x}ab', 13)

    n2 = int(f'{x}46c', 16)

    n3 = int(f'b7{x}', 15)

    value = n1 + n2 - n3

    if (value % 14) == 0:
        print(value // 14)
        break
