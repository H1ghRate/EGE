def is_triangle(dots: tuple) -> False:
    for i in range(3):
        for j in range(i + 1, 3):
            if dots[i] == dots[j]:
                return False
    
    for i in range(3):
        for j in range(i + 1, 3):
            if (dots[i][0] / dots[j][0]) == (dots[i][1] / dots[j][1]):
                return False
    
    return True
    


    
    
p1, p2, p3 = (0, 0), (0, 0), (0, 0)
p1 = (float(input()), float(input()))
p2 = (float(input()), float(input()))
p3 = (float(input()), float(input()))

if not is_triangle((p1, p2, p3)):
    print('Does not able to make triangle!')
    raise -1
else:
    ...
