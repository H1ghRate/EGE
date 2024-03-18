ABC = sorted('1234567890QWERTYUIOPASDFGHJKLZXCVBNM', reverse=True)[36-27:]

for x in ABC:
    num1 = int(f'17{x}35', 27)
    
    num2 = int(f'{x}742M', 27)
    
    num3 = int(f'{x}', 27) ** 3
    
    summa = num1 + num2 + num3
    
    if summa % 23 == 0:
        print(summa // 23)
        break
    
