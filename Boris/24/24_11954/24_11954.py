s = open('./24/24_11954/24_11954.txt').readline()

l_min = len(s) + 1

for i in s.split('Y'):
    st = end = 0

    c_x = 0

    for j in i:
        end += 1

        c_x += j == 'X'

        while c_x > 500:
            c_x -= i[st] == 'X'

            st += 1
        
        while st < len(i) and i[st] != 'X':
            st += 1
        
        if c_x >= 500:
            l_min = min(l_min, end - st)

print(l_min)
