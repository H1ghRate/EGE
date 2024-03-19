s = open('24_13085.txt').readline()

l_max = 0

st = end = 0

k_x = k_y = 0

for i in s:
    end += 1
    
    k_x += i == 'X'
    k_y += i == 'Y'


    while k_x > 1 or k_y > 1:
        k_x -= s[st] == 'X'
        k_y -= s[st] == 'Y'

        st += 1

    if k_x == 1 and k_y == 1:
        l_max = max(l_max, end - st)

print(l_max)
