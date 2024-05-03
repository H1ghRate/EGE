s = open('./24/24_13715/24_13715.txt').readline()

st = end = 0

c_ab = 0

l_max = 0

for i1, i2 in zip(s, s[1:]):
    end += 1

    c_ab += (i1 + i2) == 'AB'

    while c_ab > 50:
        c_ab -= (s[st] + s[st + 1]) == 'AB'

        st += 1
    
    if c_ab == 50:
        l_max = max(l_max, end - st)

print(l_max + 1)
