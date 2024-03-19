s = open('24/24_8567/24_8567.txt').readline()

for i in 'ABCD':
    s = s.replace(i, '*')

l0 = 0
l_max = 0
b_k = 0

for i in s:
    if i == '*':
        b_k += 1
    else:
        b_k = 0
    
    l0 += 1

    if b_k == 3:
        l_max = max(l_max, l0)
        l0 = 1

print(l_max)
