for a in range(1, 10000):
    is_ok = True

    for x in range(1, 10000):
        f = ((a + x) > (700 - a)) and (((a % 100) + (100 % x)) > 50)
        if not f:
            is_ok = False
            break
    
    if is_ok:
        print(a)
        break

