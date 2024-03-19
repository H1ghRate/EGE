s = open('24_13100.txt').readline()

l_max = 0

st = end = 0

k_c = k_d = 0

for i in s:
    end += 1

    k_c += i == 'C'
    k_d += i == 'D'


    while k_c > 2 or k_d > 2:
        k_c -= s[st] == 'C'
        k_d -= s[st] == 'D'
        
        st += 1

    l_max = max(l_max, end - st)

print(l_max)
