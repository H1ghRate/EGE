s = open('./24_11954.txt').readline()

l_min = 1e15

for si in s.split('Y'):

    st = end = 0

    c_x = 0

    for j in si:
        end += 1

        c_x += j == 'X'

        while c_x > 500:
            c_x -= j == 'X'

            st += 1

        while si[st] != si[-1] and si[st] != 'X':
            st += 1

        if c_x == 500:
            l_min = min(l_min, end - st)

print(l_min)
