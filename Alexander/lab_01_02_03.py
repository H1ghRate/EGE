from math import sin, radians

a = float(input('The first side of triangle: '))
b = float(input('The second side of triangle: '))
φ = float(input('The angles size between of them: '))

if a <= 0 or b <= 0:
    print('Lenghths of sides must be longer then zero!')
    raise 1
elif not 0 < φ < 180:
    print('The angles size must be bigger than zero and lower the one hundred eighty!')
    raise 1
else:
    square = a * b * sin(radians(φ)) / 2
    print('Square:', f'{square:.6f}')
    