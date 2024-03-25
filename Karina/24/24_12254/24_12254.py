s = open('24_12254.txt').readline()

s = s.replace('RSQ', '*')

max_rsq = 0

rsq = 0

for i in s:
    if i == '*':
        rsq += 1
    else:
        max_rsq = max(max_rsq, rsq)

        rsq = 0
    
s = s.replace('*' * max_rsq, '!')

ans = 0

for i in zip(s, s[1:], s[2:], s[3:], s[4:]):
    if i[2] == '!':
        ans = max(ans, max_rsq * 3 + (i[0] == 'S') + (i[1] == 'Q') + (i[3] == 'R') + (i[4] == 'S'))

print(ans)
