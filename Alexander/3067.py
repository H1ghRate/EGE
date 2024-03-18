s_max = int(input())

if s_max != 0:
    while (True):
        if (x := int(input())) == 0:
            break
        
        s_max = max(s_max, x)
        
    print(s_max)
else:
    print("ERROR: SEQUENCE IS EMPTY!")
    