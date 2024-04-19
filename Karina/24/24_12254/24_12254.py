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
    
s = s.replace('*' * (max_rsq - 1), '!')

ans = 0

# SQ!RS

for i in zip(s, s[1:], s[2:], s[3:], s[4:]):
    if i[2] == '!':
        left = i[1] == 'Q'
        left = left * (i[0] == 'S') + left

        right = i[3] == 'R'
        right = right * (i[3] == 'S') + right

        ans = max(ans, max_rsq * 3 + left + right)

print(ans)
