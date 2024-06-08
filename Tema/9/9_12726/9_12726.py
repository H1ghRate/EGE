with open('9_12726.csv') as f:
    for ind, i in enumerate(f, 1):
        a = list(map(int, i.split(';')))

        x3 = [i for i in a if a.count(i) == 3]

        x1 = [i for i in a if a.count(i) == 1]

        if len(x3) // 3 == 1 and len(x1) == 4:
            c_odd = c_even = 0

            for x in a:
                c_odd += (x % 2 != 0)
                c_even += (x % 2 == 0)

            if (c_even > c_odd):
                print(ind)
