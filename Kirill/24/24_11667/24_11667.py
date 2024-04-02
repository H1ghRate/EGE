with open('./24_11667/24_11667.txt') as f:
    s = f.readline()

st = 0

end = 7

c_inf = 0

l_max = 0

for i in s[7:]:
    c_inf += (''.join([s[end - i] for i in range(7, 0, -1)]) + i) == 'INFINITY'

    end += 1

    while c_inf > 1000:
        c_inf -= ''.join([s[st + i] for i in range(0, 7 + 1)]) == 'INFINITY'
        st += 1
    
    if c_inf == 1000:
        l_max = max(l_max, end - st)

print(l_max)
