with open('./9_16256.csv') as f:
    last_s = 0

    for i in f:
        a = list(map(int, i.split(';')))

        b = list(set(a))

        if len(b) == 2:
            x1 = [i for i in a if i == b[0]]

            x2 = [i for i in a if i == b[1]]

            if len(x1) >= 2 and len(x2) >= 2:
                s = sum(x1[:2]) + sum(x2[:2])
                if s < (sum(a) - s):
                    last_s = sum(a)

print(last_s)
