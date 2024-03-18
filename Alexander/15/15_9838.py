for a in range(500, -1, -1):
    is_ok = True
    for x in range(500, -1, -1):
        for y in range(500, -1, -1):
            f = (((x + 2*y) > a) or (y < x) or (x < 30))
            if not f:
                is_ok = False
                break
        if not f:
            break

    if is_ok:
        print(a)
        break
