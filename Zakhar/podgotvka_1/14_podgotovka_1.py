abc = sorted('0123456789QWERTYUIOPASDFGHJKLZXCVBNM', reverse=True)[36-22:]

for x in abc:
    num1 = int(f'98{x}79641',22)
    num2 = int(f'36{x}14',22)
    num3 = int(f'73{x}4',22)

    if (num1 + num2 + num3) % 21 == 0:
        print((num1 + num2 + num3) // 21)
        break
