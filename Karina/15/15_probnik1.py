MAX_SIZE = 20000

for a in range(MAX_SIZE, 0, -1):
    is_ok = True

    for x in range(MAX_SIZE, 0, -1):
        if (not ((x % 263 == 0) <= (x % a == 0))) and (x % 71 == 0):
            is_ok = False
            break

    if is_ok:
        print(a)
        break
