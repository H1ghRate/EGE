x_min = int(input())

if x_min != -1:
    while (x := int(input())) != -1:
        x_min = min(x_min, x)
    
    print(x_min)
else:
    print('ЧИСЕЛ НЕТ!')
