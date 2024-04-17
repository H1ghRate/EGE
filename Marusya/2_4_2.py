x_min = -1

is_first = True

while (x := int(input())) != -1:
    if x % 2 == 0 and is_first:
        x_min = x

        is_first = False
    elif x % 2 == 0:
        x_min = min(x_min, x)

if x_min == -1:
    print('ЧЕТНЫХ ЧИСЕЛ НЕТ!')
else:
    print(x_min)
    