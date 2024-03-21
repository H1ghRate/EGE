s = open('24/24_10105/24_10105.txt').readline()

st = end = 0

c_t = 0

l = 0

for i in s:
    end += 1

    c_t += i == 'T'

    while c_t > 100:
        c_t -= s[st] == 'T'
        
        st += 1

    if c_t == 100:
        l = max(l, end - st)
    

print(l)
