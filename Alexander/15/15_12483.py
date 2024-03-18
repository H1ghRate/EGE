for a in range(10000):
    is_ok = True

    for x in range(90, 100 + 1):
        f = (not ((x & 79) == 0)) and (((x & 31) == 0) <= (not ((x & a) == 0)))
        if not f:
            is_ok = False

    if is_ok:
        print(a)
        break