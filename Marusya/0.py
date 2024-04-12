# ВВОД ЧИСЕЛ А И Б
a = int(input())

b = int(input())

# АЛГОРИТМ ПРОВЕРКА НА ДЕЛЕНИЕ А НА Б
if b != 0:
    if a % b == 0:
        print('YES')
    else:
        print('NO')
else:
    print('Na nol delit nelzya!')
