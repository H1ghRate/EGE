s = open('./24/24_9552/24_example.txt').readline()

curr = ''
l = l_max = 0
b = False

for i in range(len(s)):
    curr += s[i]

    if len(curr) == 2 and curr == 'PC':
        curr = ''
        l += 2
        b = True
    elif len(curr) == 4 and curr == 'CSGO':
        curr = ''
        l += 4
        b = False
    elif len(curr) >= 4:
        l_max = max(l_max, l)
        l = 0
        curr = 'C' if b else ''
        b = False
    elif i == (len(s) - 1):
        l_max = max(l_max, l)

print(l_max)
