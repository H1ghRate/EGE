s = open('24_12254.txt').readline()

s = s.replace('RSQ', '*')

ans = 0
for n in range(15, 19):
    s_new = s.replace('*' * n, '!')

    if s_new.count('!') == 0:
        continue

    for i in zip(s_new, s_new[1:], s_new[2:], s_new[3:], s_new[4:]):
        if i[2] == '!':
            if i[1] == '*':
                left = 2
            else:
                left = i[1] == 'Q'
                left = left * (i[0] == 'S') + left

            if i[3] == '*':
                right = 2
            else:
                right = i[3] == 'R'
                right = right * (i[4] == 'S') + right

            ans = max(ans, n * 3 + left + right)

print(ans)
