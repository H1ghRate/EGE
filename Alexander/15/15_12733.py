for a in range(1, 10000):
    is_ok = True

    for y in range(10000):
        for x in range(10000):
            f = (x > 56) or (y >= x) or ((3*x - y) < a)
            if not f:
                is_ok = False
                break
        
        if not is_ok:
            break
    
    if is_ok:
        print(a)
        break
