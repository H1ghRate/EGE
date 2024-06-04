for a in range(1000, 0, -1):
    if all(((x | 26) < 42) or ((x | 36) > 68) or ((x | 12) > a) for x in range(1000, 0, -1)):
        print(a)

        break

# "|" - is just a "|", nothing more.
