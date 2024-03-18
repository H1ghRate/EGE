summa = 0
size = 0

q1 = 0
q2 = 0

while (x := int(input())) != 0:
    summa += x
    
    size += 1
    
    q1 += x ** 2
    
    q2 -= 2 * x

if size > 1:
    s = summa / size
    
    q = q1 + q2 * s + s ** 2 * size
    q = (q / (size - 1)) ** 0.5
    
    print(f'{q:.11f}')
