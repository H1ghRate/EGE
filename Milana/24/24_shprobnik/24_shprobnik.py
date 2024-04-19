s = open('24_shprobnik.txt').readline()

while 'NPO' in s:
    s = s.replace('NPO', '*')

while 'PNO' in s:
    s = s.replace('PNO', '*')

l = l_max = 0

for i in s:
    if i == '*':
        l += 1
    else:
        l_max = max(l_max, l)

        l = 0
    
print(l_max)
