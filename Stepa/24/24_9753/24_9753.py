s = open('24_9753.txt').readline()

st = end = 0

c_y = 0

l = 0

for i in s:
    end += 1

    c_y += i == 'Y'

    while c_y > 150:
        c_y -= s[st] == 'Y'

        st += 1

    l = max(l, end - st)

print(l)