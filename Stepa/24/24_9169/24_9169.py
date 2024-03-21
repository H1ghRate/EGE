s = open('24_9169.txt').readline()

s = s.replace('FAT', '*')

s = s.replace('BAD', '*')

c = 0

sts = []

l = 543243542305

for i in range(len(s)):
    if s[i] == '*':
        c += 1
        sts.append(i)
    
    if c > 3:
        sts = sts[1:]
        c -= 1

    if c == 3:
        l = min(l, i - sts[0] + 6 + 1)

print(l)
