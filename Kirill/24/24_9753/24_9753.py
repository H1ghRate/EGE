with open('./24_9753/24_9753.txt') as f:
    s = f.readline()

st = end = 0

c_y = 0

l_max = 0

for i in s:
    end += 1

    c_y += i == 'Y'

    while c_y > 150:
        c_y -= s[st] == 'Y'
        
        st += 1
    
    l_max = max(l_max, end - st)

print(l_max)
