print('Division of two numbers.')
a = int(input('a = '))

b = int(input('b = '))

if b == 0:
    print('Dividing by zero! Try again!')
else:
    c = a // b

    print(f'{a} / {b} = {c}')
