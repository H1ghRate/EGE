for x in range(1, 39):
    for y in range(1, 39):
        num = 5 * 39 ** 8 + 8 * 39 ** 7 + x * 39 ** 6 + \
        7 * 39 ** 5 + 2 * 39 ** 4 + 3 * 39 ** 3 + y * \
        39 ** 2 + 4 * 39 + 9

        if num % 38 == 0:
            yx = y * 39 + x
            
            if int(yx ** 0.5) ** 2 == yx:
                print(yx)
