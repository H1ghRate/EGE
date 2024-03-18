x_prev = int(input())

if x_prev != 0:
    counter = 0
    
    while (x := int(input())) != 0:
        counter += x > x_prev
        
        x_prev = x
        
    print(counter)
else:
    print("ERROR: SEQUENCE IS EMPTY!")
