s = open('./24_7094/24_7094.txt').readline()

s = s.replace('U', 'A')

s = s.replace('D', 'C')
s = s.replace('F', 'C')

l = 0

l_max = 0

for i in range(0, len(s) - len(s) % 2, 2):
    if s[i] != s[i + 1] and s[i] == 'C':
        l += 1
    else:
        l_max = max(l_max, l)
        l = 0

print(l_max)
