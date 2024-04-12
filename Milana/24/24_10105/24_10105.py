s = open('./24_10105/24_10105.txt').readline()

st = end = 0

l_max = 1

c_t = 0

for i in s:
    end += 1

    c_t += i == 'T'

    while c_t > 100:
        c_t -= s[st] == 'T'
        
        st += 1
    
    if c_t == 100:
        l_max = max(l_max, end - st)

print(l_max)
