s = open('24_11667.txt').readline().replace('INFINITY', '*')

l = ''

l_max = 0

st = end = 0

cnt = 0

for i in range(len(s)):
    l += s[i]

    cnt += s[i] == '*'

    while cnt > 1000:
        cnt -= s[st] == '*'
        l = l[1:]
        st += 1

    if cnt == 1000:
        l_max = max(l_max, end - st + 1)

    end += 1

print(l_max)
